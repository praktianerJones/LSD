#SPDX-License-Identifier: BSD-3-Clause
'''
urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges, J. Luelsdorf <lsd@luetze.de>

'''
from django.urls import include, path
from rest_api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
    path("licenses", views.licenses, name="rest_api_list_licenses"),
    path("licenses/<str:title>", views.licenses_single, name="rest_api_single_license"),
    path(
        "licenses/<str:title>/releases",
        views.licenses_all_associated_releases,
        name="rest_api_license_releases",
    ),
    path("packages", views.packages, name="rest_api_list_packages"),
    path(
        "packages/<str:package_name>/versions/<str:package_version>",
        views.packages_by_name_and_version,
        name="rest_api_single_package",
    ),
    path("products", views.product_list),
    path("products/<str:article_number>", views.product_by_number),
    path("products/<str:article_number>/revisions/latest", views.product_latest),
    path(
        "products/<str:article_number>/revisions/<int:article_revision>", views.product
    ),
    path("releases", views.release_list),
    path(
        "releases/<str:release_nr>",
        views.release_by_number,
        name="rest_api_single_release",
    ),
]
