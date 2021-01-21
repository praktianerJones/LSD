# SPDX-License-Identifier: BSD-3-Clause
'''
views.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import status
from software.models import Release
from licenses.models import Section, License, Paragraph
from licenses.forms import LicensesRegisterForm


@login_required(login_url="/login")
def license_add(request):
    """
    An authenticated User can add a license,
    if they are authenticated and fills the form with valid information.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    if request.method == 'POST':
        temp = request.FILES
        print(temp['originalText'].read().decode())
        '''
        Checks if input data is a valid LicenseRegisterForm, if it is unique and adds it to the database. 
        A success message is displayed and the license is added. If the check is negativ the license is not added and a warning message is displayed.
        ''' 
        license_dic = request.POST.dict()
        filename = request.FILES["originalText"].name
        license_dic["request_User"] = request.user.id
        form = LicensesRegisterForm(license_dic, request.FILES)
        if filename.endswith(".txt") or filename.endswith(".pdf"):
            if form.is_valid():
                title = form.cleaned_data.get("title")
                if not License.objects.all().filter(title=title):
                    form.save()
                    messages.success(request, f"License added {title}")
                    # Status code on redirect is 302
                    return redirect("license-list")

                messages.warning(
                    request, "A license with that title already exists."
                )
                status_code = status.HTTP_409_CONFLICT
        else:
            messages.warning(request, "Please upload a pdf or txt file.")
            status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    elif request.method == "GET":
        # The form is loaded as an empty form, when the User starts or refreshes the page.
        form = LicensesRegisterForm()
        status_code = status.HTTP_200_OK
    return render(
        request, "licenses/license_add.html", {"form": form}, status=status_code
    )


def license_list(request):
    """
    The function returns a list of all licenses.
    The license list can be filtered through user input.
    """
    filter_dic = request.GET
    license_list_all= License.objects.all()
    license_list_temp = []
    # Check if dictionary is empty
    # Filters list according to search
    if filter_dic:

        # The three if's work in the same schematics
        #   1. Check if filter is set
        #   2. Get all licenses and filter them by querry, put them in a temp list
        #   3. Turn templist and licenselist to sets check the doublicates and overwrite licenselist

        # Lead to MultiValueDictKeyError if not checked redundantly
        if "permission_level" in filter_dic and filter_dic["permission_level"] != "":
            license_list_temp = License.objects.all().filter(
                permission_level_license=get_permission_level_int(
                    filter_dic.get("permission_level")
                )
            )
            license_list_all = list(set(license_list_all) & set(license_list_temp))

        if filter_dic["license_title"] != "":
            license_list_temp = License.objects.all().filter(
                title__contains=filter_dic.get("license_title")
            )
            license_list_all = list(set(license_list_all) & set(license_list_temp))

        if filter_dic["release_title"] != "":
            license_list_temp = []
            # Get a list of releases which contain the release_title
            release_list_temp = Release.objects.all().filter(
                title__contains=filter_dic.get("release_title")
            )
            # pull out all licenses which are used by any of the release_list
            for release_item in release_list_temp:
                for license_temp in release_item.linked_licenses.all():
                    license_list_temp.append(license_temp)
            license_list_all = list(set(license_list_all) & set(license_list_temp))

    context = {"licenses": license_list_all}
    return render(request, "licenses/license_list.html", context)


def license_details(request, license_title):
    """
    Return the license with the requested title.
    Show informations like information of the license and
    the Releases which use the returned license
    """
    requested_license = License.objects.filter(title=license_title)[0]
    context = {"license": requested_license}

    release_list = Release.objects.all()
    release_list_temp = list(release_list)
    for release in release_list:
        if not release.linked_licenses.filter(id=requested_license.id):
            release_list_temp.remove(release)
    context["releases_which_use_license"] = release_list_temp

    return render(request, "licenses/license_detail.html", context)


def original_license(request, license_title):
    """
    This function shows the original license, which is stored in the folder media/TextFileLicenses
    """
    try:
        license_temp = License.objects.filter(title=license_title)[0]
        cur_dir = os.path.dirname(__file__)
        path = os.path.join(cur_dir, "../media/" + str(license_temp.originalText))
        if path.endswith("txt"):
            with open(path, "r") as txt:
                response = txt.read()
                txt.close()
                context = {"original": response}
            return render(request, "licenses/license_view_original.html", context)

        if path.endswith("pdf"):
            with open(path, "rb") as pdf:
                response = HttpResponse(pdf.read(), content_type="application/pdf")
                response["Content-Disposition"] = "inline;filename=some_file.pdf"
                pdf.close()
                return response

        else:
            messages.warning(request, "The requested File should be pdf or txt.")
            return render(request, "licenses/license_list.html")
    except IndexError:
        messages.warning(request, "A license with that title does not exist.")
        return render(request, "licenses/license_list.html")


def download_license(license_title):
    """
    This function lets the user download the original license as a text file.
    The license is saved in the Folder media/TextFileLicenses
    """
    temp_license = License.objects.filter(title=license_title)[0]
    cur_dir = os.path.dirname(__file__)
    path = os.path.join(cur_dir, "../media/" + str(temp_license.originalText))
    response = HttpResponse(open(path, "rb"), content_type="text/plain")
    # Allows to download the file, otherwise it would be shown in browser
    response["Content-Disposition"] = "attachement; filename=%s" % str(
        temp_license.originalText.name
    )
    return response


def section_details(request, section_pk):
    """
    Function not used yet, will be display paragraph(s)
    of a section.
    """
    context = {"section": Section.objects.filter(id=section_pk)[0]}
    return render(request, "licenses/section_detail.html", context)


def paragraph_details(request, paragraph_pk):
    """
    Function not used yet, will be display paragraph(s)
    of a section.
    """
    context = {"paragraph": Paragraph.objects.filter(id=paragraph_pk)[0]}
    return render(request, "licenses/paragraph_detail.html", context)


####################### Help Functions #######################

def get_permission_level_int(permission_level):
    """
    Help Function for license_list
    """
    if permission_level == "RED":
        return 0
    if permission_level == "YELLOW":
        return 1
    if permission_level == "GREEN":
        return 2
    return 0
