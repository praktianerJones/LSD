#SPDX-License-Identifier: BSD-3-Clause
'''
urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges <lsd@luetze.de>
'''
from django.urls import path
from tools import views

urlpatterns = [
    path("", views.tools_list, name="tools-list"),
    path("<str:tool_name>", views.tool_version_list, name="tool-version-list"),
    path("<str:tool_name>/<str:tool_version>", views.tool_details, name="tool-details"),
]
