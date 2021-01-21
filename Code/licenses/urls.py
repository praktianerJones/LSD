#SPDX-License-Identifier: BSD-3-Clause
'''
urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>

'''
from django.urls import path
from licenses import views

urlpatterns = [
    path("", views.license_list, name="license-list"),
    path("add", views.license_add, name="license-add"),
    path("<str:license_title>", views.license_details, name="license-details"),
    path(
        "<str:license_title>/original", views.original_license, name="original-license"
    ),
    path(
        "<str:license_title>/download", views.download_license, name="license-download"
    ),
    path(
        "paragraphs/<str:paragraph_pk>",
        views.paragraph_details,
        name="paragraph-details",
    ),
    path("sections/<str:section_pk>", views.section_details, name="section-details"),
]
