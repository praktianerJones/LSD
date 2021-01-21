#SPDX-License-Identifier: BSD-3-Clause
'''
urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, J. Luelsdorf <lsd@luetze.de>
'''
from django.urls import path
from software import views

urlpatterns = [
    path("", views.software_list, name="software-list"),
    path("<str:software_name>", views.software_details, name="software-detail"),
    path("<str:software_name>/change",
        views.software_details_change,
        name="software-detail-change",
    ),
    path(
        "<str:software_name>/latest",
        views.software_details_latest,
        name="software-datail-latest",
    ),
    path(
        "<str:software_name>/nightly",
        views.software_details_nightly,
        name="software-detail-nightly",
    ),
    path(
        "<str:software_name>/<str:software_version>",
        views.software_details_version,
        name="software-detail-version",
    ),
    path(
        "<str:software_name>/<str:software_version>/release",
        views.software_details_version_release,
        name="software-detail-version-release",
    ),
    path(
        "<str:software_name>/<str:software_version>/withdraw",
        views.software_details_version_withdraw,
        name="software-detail-version-withdraw",
    ),
    path(
        "<str:software_name>/<str:software_version>/addLicense",
        views.add_license_to_release,
        name="add_license_to_release",
    ),
]
