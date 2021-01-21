#SPDX-License-Identifier: BSD-3-Clause

'''
views.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges, J. Luelsdorf <lsd@luetze.de>

'''
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from licenses.models import License
from software.models import Release
from products.models import Product
from packages.models import Package
from rest_api.serializer import (
    ReleaseSerializer,
    ProductSerializer,
    LicenseSerializer,
    PackageSerializer,
)

############################## Release ##############################################
@api_view(["GET", "POST"])
def release_list(request):
    """
    List all releases, or create a new release.
    """
    if request.method == "GET":
        releases = Release.objects.all()
        serializer = ReleaseSerializer(releases, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ReleaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["laste_edited_by"] = User.objects.first()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def release_by_number(request, release_nr):
    """
    get a single release by number
    """
    if request.method == "GET":
        releases = Release.objects.filter(id=release_nr)
        serializer = ReleaseSerializer(releases, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)



################################# Product ##############################################
# get all releases used in latest Revision of given article number
@api_view(["GET"])
def product_latest(request, article_number):
    """
    List the latest release of article_number.
    """
    if request.method == "GET":
        product_temp_list = []
        product_temp_list = Product.objects.filter(article_number=article_number).order_by(
            "-article_revision"
        )[0]
        if product_temp_list is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        linked_software = product_temp_list.linked_software.all()
        serializer = ReleaseSerializer(linked_software, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_by_number(request, article_number):
    """
    List all products with article_number and identify Releases, Families and by ID.
    """
    if request.method == "GET":
        products = Product.objects.order_by("-article_revision").filter(
            article_number=article_number
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def product(request, article_number, article_revision):
    """
    List all releases corresponding to article_number with article_revision.
    """
    if request.method == "GET":
        product_temp_list = Product.objects.get(
            article_number=article_number, article_revision=article_revision
        )
        if product_temp_list is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        linked_software = product_temp_list.linked_software.all()
        serializer = ReleaseSerializer(linked_software, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "POST"])
def product_list(request):
    """
    List all products and identify Releases, Families and by ID.
    """
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # TODO: It needs to be checked wether an articleNo with the given revision does exist
    #       Input Validation of all inputs should be tested and implemented if necessary
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["author"] = User.objects.first()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)



###################################### Licenses #########################################


@api_view(["GET"])
def licenses(request):
    """
    return all licenses
    """
    if request.method == "GET":
        licenses_list = License.objects.all()
        serializer = LicenseSerializer(licenses_list, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def licenses_single(title):
    """
    Return a single license with the according title
    """
    license_temp = License.objects.filter(title=title)
    serializer = LicenseSerializer(license_temp, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def licenses_all_associated_releases(request, title):
    """
    Return all releases associated with a single license
    """
    if request.method == "GET":
        license_temp = License.objects.get(title=title)
        if license_temp is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # checks if release has a linked license and ads release to
        # linked_releases if that's true
        linked_releases = []
        for release in Release.objects.all():
            for linked_license in release.linked_licenses.all():
                if linked_license == license_temp:
                    linked_releases.append(release)
                    continue

        serializer = ReleaseSerializer(linked_releases, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_201_CREATED)


################################ Packages #############################################


@api_view(["GET", "POST"])
def packages(request):
    """
    Return a list of all packages or add a list of packages
    """
    if request.method == "GET":
        package_list = Package.objects.all()
        serializer = PackageSerializer(package_list, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        package_license_used_differ = []
        package_already_in_database = []
        package_wants_to_use_unknown_license = []
        package_added_to_database = []
        packagereturn = {}

        # Iterate through all recieved Packages and sort them into one of the four above lists
        for package_dic in request.data:
            # changes the KEY's of the packageDic into Lowercases
            package_dic = dict((k.lower(), v) for k, v in package_dic.items())
            # Case_1 Package is already in Database
            if Package.objects.filter(package_name=package_dic["package_name"]).filter(
                package_version=package_dic["package_version"]
            ):
                package_from_database = Package.objects.filter(
                    package_name=package_dic["package_name"]
                ).filter(package_version=package_dic["package_version"])[0]
                # Case_1_1 Package already in Database but is using another used_license or has no used_license
                if package_dic["license_used"]:
                    if not (
                        package_from_database.license_used.title
                        == package_dic["license_used"]
                    ) or not package_dic["license_used"] in package_dic["license_list"]:
                        package_license_used_differ.append(package_dic)
                    # Case_1_2 Package Is in Database and doesnt differ
                    else:
                        package_already_in_database.append(package_dic)
            # Case_2 Package is not in Database yet
            else:
                # Case_2_1 Package is using a license which is not in the Database
                if not are_all_licenses_in_database(package_dic):
                    package_wants_to_use_unknown_license.append(package_dic)
                # Case_2_2 Package can be added to the Database
                else:
                    package_added_to_database.append(package_dic)
        # Add all Packages which are added to the package_added_to_database to the Database
        serializer = PackageSerializer(data=package_added_to_database, many=True)
        if serializer.is_valid():
            serializer.save()

            # Return all four lists of Packages in one dictionary and return it to the LBS
            packagereturn[
                "Packages where added to the Database"
            ] = package_added_to_database
            packagereturn[
                "Packages where the license used differ"
            ] = package_license_used_differ
            packagereturn[
                "Packages where not added to the Database, they were already in the Database"
            ] = package_already_in_database
            packagereturn[
                "Packages wants to use unknown License"
            ] = package_wants_to_use_unknown_license
            return Response(packagereturn, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def packages_by_name_and_version(package_name, package_version):
    """
    Return a package by Name and Version.
    """
    package_list = Package.objects.filter(package_name=package_name)
    package_list_version = package_list.get(package_version=package_version)
    serializer = PackageSerializer(package_list_version)
    return Response(serializer.data)

def are_all_licenses_in_database(package_dic):
    """
    Helpfunctions for Packages Post Request.
    """
    for license_title in package_dic["license_list"]:
        if not License.objects.filter(title=license_title):
            return False
    return True
