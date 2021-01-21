# SPDX-License-Identifier: BSD-3-Clause
"""
urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges, J. Luelsdorf <lsd@luetze.de>
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", include("lsd.urls")),
    path("admin/", admin.site.urls),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="lsd/login.html"),
        name="login",
    ),
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="/software/"), name="logout"
    ),
    path("licenses/", include("licenses.urls")),
    path("products/", include("products.urls")),
    path("rest_api/", include("rest_api.urls")),
    path("software/", include("software.urls")),
    path("tools/", include("tools.urls")),
    path("va/", include("va.urls"))

]
