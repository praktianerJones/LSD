#SPDX-License-Identifier: BSD-3-Clause

'''
views.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Hentges, J. Luelsdorf <lsd@luetze.de>
'''
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.db import IntegrityError
from software.models import Release
from software.forms import ReleaseAddLicenseForm


def software_list(request):
    """
    Renders a template with a list of every software.
    """
    release_list = []
    release_title_list = []
    for release in Release.objects.all():
        if release.title not in release_title_list:
            release_title_list.append(release.title)
            release_list.append(release)

    context = {"softwares": release_list}
    return render(request, "software/software_list.html", context)


def software_details(request, software_name):
    """
    Renders a template with a single software with a specific software_name
    """
    context = {
        "releases": Release.objects.order_by("-date").filter(title=software_name)
    }
    return render(request, "software/software_releases_details.html", context)


def software_details_change(request, software_name):
    """
    Loads a form to add a used license to the software.
    """
    if request.user.is_authenticated:
        if request.method == "POST":
            releases = Release.objects.order_by("-date").filter(title=software_name)
            for release in releases:

                if not license in release.linked_licenses.all():
                    release.linked_licenses.add(license)
                    release.save()
            return redirect("software-detail", software_name=software_name)
        form = ReleaseAddLicenseForm()
        return render(request, "software/releaseAddLicenseForm.html", {"form": form})
    return render(request, "lsd/unauthenticated_User_page.html")


def software_details_latest(request, software_name):
    """
    Displaies the latest software which was released.
    !Carefull, when a software hasn't the status r, the
    User won't be redirected.
    """
    context = {
        "release": Release.objects.order_by("-date").filter(
            title=software_name, status="r"
        )[0]
    }
    return render(request, "software/software_release_details.html", context)


def software_details_nightly(request, software_name):
    """
    Shows latest pushed Software.
    """
    context = {
        "release": Release.objects.order_by("-date").filter(title=software_name)[0]
    }
    return render(request, "software/software_release_details.html", context)


def software_details_version(request, software_name, software_version):
    """
    Renders a software with a specific name and version.
    """
    context = {
        "release": Release.objects.order_by("-date").filter(
            title=software_name, version_string=software_version
        )[0]
    }
    return render(request, "software/software_release_details.html", context)


def software_details_version_release(request, software_name, software_version):
    """
    Changes the release status of a specific software version to released.
    """
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    release = Release.objects.order_by("-date").filter(
        title=software_name, version_string=software_version
    )[0]
    release.status = "r"
    release.save()
    return redirect("/software/{}/{}".format(software_name, software_version))


def software_details_version_withdraw(request, software_name, software_version):
    """
    Changes the release status of a specific software version to withdrawn.
    """
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    release = Release.objects.order_by("-date").filter(
        title=software_name, version_string=software_version
    )[0]
    release.status = "w"
    release.save()
    return redirect("/software/{}/{}".format(software_name, software_version))


def add_license_to_release(request, software_name, software_version):
    """
    An authenticated User can choose an existing License and add it to a Software Release
    """
    if request.user.is_authenticated:

        if request.method == "POST":
            try:
                release = Release.objects.filter(
                    title=software_name, version_string=software_version
                )[0]
                linked_licenses = request.POST.dict()["linked_licenses"]
                release.linked_licenses.add(linked_licenses)
                messages.success(request, "License(s) added to Release")
                return redirect(
                    "software-detail-version",
                    software_name=software_name,
                    software_version=software_version,
                )
            except KeyError:
                form = ReleaseAddLicenseForm()
                messages.warning(request, "Please choose a license from the box.")
                return render(request, "software/releaseAddLicenseForm.html", {"form": form})
            except IntegrityError:
                form = ReleaseAddLicenseForm()
                messages.warning(request, "A license with that title already exists in Release.")
                return render(request, "software/releaseAddLicenseForm.html", {"form": form})

        elif request.method == "GET":
            form = ReleaseAddLicenseForm()
            return render(request, "software/releaseAddLicenseForm.html", {"form": form})

    return render(request, "lsd/unauthenticated_User_page.html")
