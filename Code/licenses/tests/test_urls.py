#SPDX-License-Identifier: BSD-3-Clause
'''
test_urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from licenses.views import (
    license_list,
    license_details,
    license_add,
    original_license,
    download_license,
)


class TestUrls(SimpleTestCase):
    """
    All URL's from the license App are tested here.
    The according url has a global name, which can be reversed to its http link.
    If the name can be reversed and called the test is sucessful.
    """

    def test_license_view_license_list(self):
        url = reverse("license-list")
        self.assertEquals(resolve(url).func, license_list)

    def test_license_add(self):
        url = reverse("license-add")
        self.assertEquals(resolve(url).func, license_add)

    def test_license_view_license_details(self):
        url = reverse("license-details", args=["default"])
        self.assertEquals(resolve(url).func, license_details)

    def test_license_view_original(self):
        url = reverse("original-license", args=["license1"])
        self.assertEquals(resolve(url).func, original_license)

    def test_download_license(self):
        url = reverse("license-download", args=["license1"])
        self.assertEquals(resolve(url).func, download_license)
