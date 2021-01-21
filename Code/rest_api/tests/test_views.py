#SPDX-License-Identifier: BSD-3-Clause


'''
test_views.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
import json
from django.contrib.auth.models import User
from licenses.models import License
from packages.models import Package
from software.models import Release


class TestRestApiViews(TestCase):
    """
    All functional Methods from the rest_api App are tested here.
    After the database is setUp each method tests one function of the View.
    It is checked if the method returns the correct response status and forwards the user onto the correct template.
    """

    #############################set Up###################################################
    def setUp(self):
        self.client = Client()
        ############################add User to Database######################################
        self.user1 = User.objects.create_user(
            username="user1",
            email="user1@mail.com",
            password="test",
        )
        ###########################add Licenses to Database###################################
        self.license1 = License.objects.create(
            title="License_test",
            permission_level_license="2",
            annotation="This is a test license",
            originalText="tests/License_test.txt",
            request_User=self.user1,
        )
        self.license2 = License.objects.create(
            title="License_test_differ",
            permission_level_license="2",
            annotation="This is a test license",
            originalText="tests/License_test.txt",
            request_User=self.user1,
        )
        ##########################add Releases to Database####################################
        self.release_dummy = Release.objects.create(
            title="Release_test",
            version_string="V0000",
            version_major=1,
            version_minor=2,
            version_micro=2,
            version_build=1,
            version_commit="True",
            git_path="Test/Path",
            bin_path="Dummy/Path",
            doc_path_html="does not exist",
            doc_path_pdf="shouldnt that be a file",
        )
        self.release_dummy.linked_licenses.add(self.license1)
        ##########################add Packages to Database####################################
        self.package1 = Package.objects.create(
            package_name="TestPackage",
            package_version="V1",
            package_description="This is a package",
            package_creator=self.user1,
            license_used=self.license1,
        )
        self.package2 = Package.objects.create(
            package_name="TestPackage2",
            package_version="V1",
            package_description="This is a package",
            package_creator=self.user1,
            license_used=self.license1,
        )
        self.package3 = Package.objects.create(
            package_name="AlreadyinDatabase",
            package_version="1",
            package_description="This Package is already in the DB",
            usage="u",
            package_creator=self.user1,
            license_used=self.license1,
        )
        self.package3.license_list.add(self.license1)
        self.package4 = Package.objects.create(
            package_name="License_used_differ",
            package_version="1",
            package_description="This Package is already in the DB with a different license_used",
            package_creator=self.user1,
            license_used=self.license1,
        )
        #########################All URL's are reversed here (global name and argument of call)##
        self.license_single_url = reverse(
            "rest_api_single_license", args=["License_test"]
        )
        self.license_list_url = reverse("rest_api_list_licenses")
        self.license_associated_url = reverse(
            "rest_api_license_releases", args=["License_test"]
        )
        self.package_single_url = reverse(
            "rest_api_single_package", args=["TestPackage", "V1"]
        )
        self.package_list_url = reverse("rest_api_list_packages")

    ###########################Test release_list#############################################
    ###########################Test release_by_number#########################################
    ###########################Test product_latest########################################
    ###########################Test product_by_number########################################
    ###########################Test product#############################################
    ###########################Test product_list#############################################

    ###########################Test licenses GET#############################################
    def test_license_succeding_list_all_licenses(self):
        response = self.client.get(self.license_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data[0]["title"], "License_test")

    ###########################Test licenses_single GET#############################################
    def test_licenses_single_succeding_single_license(self):
        response = self.client.get(self.license_single_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data[0]["title"], "License_test")

    ###########################Test licenses_all_associated_releases#############################################
    def test_GET_licenses_associated_releases(self):
        response = self.client.get(self.license_associated_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.data[0]["linked_licenses"][0]["title"], "License_test"
        )
        self.assertEquals(response.data[0]["title"], "Release_test")

    ###########################Test packages GET#############################################
    def test_packages_succeding_package_list(self):
        response = self.client.get(self.package_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data[0]["package_name"], "TestPackage")
        self.assertTrue(response.data[1]["package_name"], "TestPackage2")

    ###########################Test packages POST#############################################
    def test_packages_succeding_added_to_DB(self):
        list_json = TestRestApiViews.get_List_of_Packages(self)
        response = self.client.post(
            self.package_list_url,
            data=json.JSONEncoder().encode(list_json),
            content_type="application/json",
        )
        self.assertEquals(
            response.data["Packages where added to the Database"][0]["package_name"],
            "TestAddtoDB",
        )

    def test_packages_failing_license_used_differ(self):
        list_json = TestRestApiViews.get_List_of_Packages(self)
        response = self.client.post(
            self.package_list_url,
            data=json.JSONEncoder().encode(list_json),
            content_type="application/json",
        )
        self.assertEquals(
            response.data["Packages where the license used differ"][0]["package_name"],
            "License_used_differ",
        )

    def test_packages_failing_package_already_in_DB(self):
        list_json = TestRestApiViews.get_List_of_Packages(self)
        response = self.client.post(
            self.package_list_url,
            data=json.JSONEncoder().encode(list_json),
            content_type="application/json",
        )
        self.assertEquals(
            response.data[
                "Packages where not added to the Database, because they were already in the Database"
            ][0]["package_name"],
            "AlreadyinDatabase",
        )

    def test_packages_failing_wants_to_use_unkown_License(self):
        list_json = TestRestApiViews.get_List_of_Packages(self)
        response = self.client.post(
            self.package_list_url,
            data=json.JSONEncoder().encode(list_json),
            content_type="application/json",
        )
        self.assertEquals(
            response.data["Packages wants to use unknown License"][0]["package_name"],
            "Invalid_License",
        )

    ###########################Test packages_by_name_and_version GET#############################################
    def test_packages_by_name_and_version_succeding_package_single(self):
        response = self.client.get(self.package_single_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data["package_name"], "TestPackage")

    @staticmethod
    def get_List_of_Packages(self):
        list_of_packages = (
            {
                "package_name": "TestAddtoDB",
                "package_version": "1",
                "package_description": "This is a test",
                "usage": "u",
                "date": "2020-10-30T13:31:07Z",
                "package_creator": 1,
                "license_list": ["License_test"],
                "license_used": "License_test",
            },
            {
                "package_name": "License_used_differ",
                "package_version": "1",
                "package_description": "This Package is already in the DB with a different license_used",
                "usage": "u",
                "date": "2020-10-30T13:31:07Z",
                "package_creator": 1,
                "license_list": ["License_test", "License_test_differ"],
                "license_used": "License_test_differ",
            },
            {
                "package_name": "Invalid_License",
                "package_version": "1",
                "package_description": "This is a test",
                "usage": "u",
                "date": "2020-10-30T13:31:07Z",
                "package_creator": 1,
                "license_list": ["An_Invalid_License"],
                "license_used": "An_Invalid_License",
            },
            {
                "package_name": "AlreadyinDatabase",
                "package_version": "1",
                "package_description": "This Package is already in the DB",
                "usage": "u",
                "date": "2020-10-30T13:31:07Z",
                "package_creator": 1,
                "license_list": ["License_test"],
                "license_used": "License_test",
            },
        )
        return list_of_packages
