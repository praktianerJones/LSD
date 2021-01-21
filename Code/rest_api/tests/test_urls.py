#SPDX-License-Identifier: BSD-3-Clause


'''
test_urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_api.views import (
    release_by_number,
    packages,
    packages_by_name_and_version,
    licenses,
)


class TestRestApiUrls(SimpleTestCase):
    """
    All URL's from the rest_api App are tested here.
    The according url has a global name, which can be reversed to its http link.
    If the name can be reversed and called the test is sucessful.
    """

    def test_single_release_url_resolves(self):
        url = reverse("rest_api_single_release", args=["1"])
        self.assertEquals(resolve(url).func, release_by_number)

    def test_list_licenses_url_resolves(self):
        url = reverse("rest_api_list_licenses")
        self.assertEquals(resolve(url).func, licenses)

    def test_list_packages_url_resolves(self):
        url = reverse("rest_api_list_packages")
        self.assertEquals(resolve(url).func, packages)

    def test_single_package_url_resolves(self):
        url = reverse("rest_api_single_package", args=["packetname", "versionsnummer"])
        self.assertEquals(resolve(url).func, packages_by_name_and_version)

    def test_post_list_packages_url_resolves(self):
        url = reverse("rest_api_list_packages")
        self.assertEquals(resolve(url).func, packages)
