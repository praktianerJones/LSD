#SPDX-License-Identifier: BSD-3-Clause
'''
views.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges, J. Luelsdorf <lsd@luetze.de>

'''
import re
from django.shortcuts import render, redirect, reverse
from software.models import Release


def home(request):
    """
    This function loads the home page.
    """
    context = {"releases": Release.objects.order_by("-date").all()}
    return render(request, "lsd/home.html", context)


def project(request, project_name):
    """
    This function returns releases, which have a specific project name
    ordered by date.
    """
    context = {
        "releases": Release.objects.order_by("-date").filter(
            title__startswith=project_name
        )
    }
    return render(request, "lsd/home.html", context)

def about(request):
    """
    This function is not in use at the momement, it will be used to
    give information about the Website, its deployer and general information.
    """
    return render(request, "lsd/about.html", {"title": "About"})
