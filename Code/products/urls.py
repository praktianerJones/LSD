#SPDX-License-Identifier: BSD-3-Clause
'''
urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Hentges, J. Luelsdorf <lsd@luetze.de>
'''
from django.urls import path
from products import views

# CAUTION!
# string/staticString/ has to be defined before any occurence of string/<str:variableName>/ otherwise
# staticString would be interpreted as <str:variableName>

urlpatterns = [
    path("", views.product_list, name="product-list"),
    path("<str:article_number>", views.product_details, name="product-details"),
    path(
        "<str:article_number>/revisions/latest",
        views.product_details_latest,
        name="product-details-latest",),
    path(
        "<str:article_number>/revisions/<str:article_revision>",
        views.product_details_revision,
        name="product-details-revision",),
]
