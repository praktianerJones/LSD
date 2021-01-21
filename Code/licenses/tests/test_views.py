#SPDX-License-Identifier: BSD-3-Clause
'''
test_views.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from licenses.models import License
from software.models import Release
from rest_framework import status
import tempfile, shutil
from django.utils import timezone

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestViews(TestCase):
    """
    All functional Methods from the license App are tested here.
    After the database is setUp each method tests one function of the View.
    It is checked if the method returns the correct response status and forwards the user onto the correct template.
    """

    ###############################SetUp######################################################
    def setUp(self):
        self.client = Client()
        ###############################Add User into Database#####################################
        self.dummyUser = User.objects.create_user(
            username="TestUser", email="TestUser@mail.com", password="test"
        )
        ###############################Add License into Database##################################
        self.license_dummy = License.objects.create(
            title="License_test",
            permission_level_license=0,
            annotation="gibet nicht",
            originalText="tests/License_test.txt",
            request_User=self.dummyUser,
        )
        self.license_pdf_dummy = License.objects.create(
            title="License_with_PDF",
            permission_level_license=0,
            annotation="Still nothing",
            originalText="tests/License_test.pdf",
            request_User=self.dummyUser,
        )
        self.license_wrong_filetype_dummy = License.objects.create(
            title="License_wrong_filetype",
            permission_level_license=0,
            annotation="So much more of nothing that the old narrator had enough and they had to hire a new one.",
            originalText="tests/License_test.rst",
            request_User=self.dummyUser,
        )
        ###############################Add Release into Database##################################
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
        self.release_dummy.linked_licenses.add(self.license_dummy)
        ###############################Set Routes for Testing#####################################
        self.license_list_url = reverse("license-list")
        self.license_details_url = reverse("license-details", args=["License_test"])
        self.license_original_url = reverse("original-license", args=["License_test"])
        self.license_original_pdf_url = reverse(
            "original-license", args=["License_with_PDF"]
        )
        self.license_original_none_existing_url = reverse(
            "original-license", args=["There_is_no_File"]
        )
        self.license_original_wrong_filetype_url = reverse(
            "original-license", args=["License_wrong_filetype"]
        )
        self.license_download_url = reverse("license-download", args=["License_test"])
        self.license_add_url = reverse("license-add")

    ###############################Test license_add###########################################
    def test_license_add_succeding_add_license(self):
        self.client.login(username="TestUser", password="test")
        with open("djangoProject/media/tests/License_test.txt") as fp:
            response = self.client.post(
                self.license_add_url,
                {
                    "title": "A_new_License_test",
                    "permission_level_license": "0",
                    "annotation": "gibet nicht",
                    "originalText": fp,
                },
            )
        self.assertEquals(response.status_code, status.HTTP_302_FOUND)
        self.assertEquals(
            License.objects.filter(title="A_new_License_test")[0].title,
            "A_new_License_test",
        )

    def test_license_add_failing_User_not_logged_In(self):
        with open("djangoProject/media/tests/License_test.txt") as fp:
            response = self.client.post(
                self.license_add_url,
                {
                    "title": "A_new_License_test",
                    "permission_level_license": "0",
                    "annotation": "gibet nicht",
                    "originalText": fp,
                    "falscheForm": "Domine",
                },
            )
        self.assertFalse(License.objects.filter(title="A_new_License_test").exists())

    def test_license_add_failing_license_already_exists(self):
        self.client.login(username="TestUser", password="test")
        with open("djangoProject/media/tests/License_test.txt") as fp:
            response = self.client.post(
                self.license_add_url,
                {
                    "title": "License_test",
                    "permission_level_license": "0",
                    "annotation": "gibet nicht",
                    "originalText": fp,
                },
            )
        self.assertEquals(response.status_code, status.HTTP_409_CONFLICT)

    def test_license_add_failing_wrong_file_type(self):
        self.client.login(username="TestUser", password="test")
        with open("djangoProject/media/tests/File_with_wrong_Type.rst") as fp:
            response = self.client.post(
                self.license_add_url,
                {
                    "title": "License_test",
                    "permission_level_license": "0",
                    "annotation": "gibet nicht",
                    "originalText": fp,
                },
            )
        self.assertEquals(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    def test_license_add_succeding_load_form(self):
        self.client.login(username="TestUser", password="test")
        response = self.client.get(self.license_add_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    ###############################Test license_details#######################################
    def test_license_details_succeding_load_licenses(self):
        response = self.client.get(self.license_details_url)
        self.assertEquals(response.templates[0].name, "licenses/license_detail.html")
        self.assertEquals(response.context["license"].title, "License_test")

    def test_license_details_failing_load_licenses(self):
        response = self.client.get(self.license_details_url)
        self.assertNotEquals(response.templates[0].name, "licenses/license_list.html")
        self.assertNotEquals(response.context["license"].title, "WrongLicenseTitle")

    def test_license_details_succeding_load_licenses_with_linked_release(self):
        response = self.client.get(self.license_details_url)
        self.assertEquals(
            response.context["releases_which_use_license"][0].title, "Release_test"
        )

    ###############################Test original_license######################################
    def test_original_license_succeding_load_txt_file_in_Webpage(self):
        response = self.client.get(self.license_original_url)
        self.assertEquals(
            response.templates[0].name, "licenses/license_view_original.html"
        )
        with open("djangoProject/media/tests/License_test.txt", "r") as txt:
            self.assertEquals(response.context["original"], txt.read())
            txt.close()

    def test_original_license_succeding_load_pdf_file_in_Webpage(self):
        response = self.client.get(self.license_original_pdf_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        with open("djangoProject/media/tests/License_test.pdf", "rb") as pdf:
            self.assertEquals(response.content, pdf.read())
            pdf.close()

    def test_original_license_failing_license_not_in_MediaFolder(self):
        response = self.client.get(self.license_original_none_existing_url)
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")

    def test_original_license_failing_license_has_wrong_file_ending(self):
        response = self.client.get(self.license_original_wrong_filetype_url)
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")

    ###############################Test license_list##########################################
    def test_license_list_succeding_load_licenses(self):
        response = self.client.get(self.license_list_url)
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")
        self.assertTrue(self.license_dummy in response.context["licenses"])

    def test_license_list_failing_permission_filter(self):
        response = self.client.get(
            self.license_list_url,
            {"permission_level": "YELLOW", "license_title": "", "release_title": ""},
        )
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")
        self.assertFalse(self.license_dummy in response.context["licenses"])

    def test_license_list_succeding_permission_filter(self):
        response = self.client.get(
            self.license_list_url,
            {"permission_level": "RED", "license_title": "", "release_title": ""},
        )
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")
        self.assertTrue(self.license_dummy in response.context["licenses"])

    def test_license_list_succeding_license_title(self):
        response = self.client.get(
            self.license_list_url,
            {
                "permission_level": "",
                "license_title": "License_test",
                "release_title": "",
            },
        )
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")
        self.assertTrue(self.license_dummy in response.context["licenses"])

    def test_license_list_failing_license_title(self):
        response = self.client.get(
            self.license_list_url,
            {
                "permission_level": "",
                "license_title": "Thats_not_a_Title",
                "release_title": "",
            },
        )
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")
        self.assertFalse(self.license_dummy in response.context["licenses"])

    def test_license_list_failing_release_title(self):
        response = self.client.get(
            self.license_list_url,
            {
                "permission_level": "",
                "license_title": "",
                "release_title": "Release_test",
            },
        )
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")
        self.assertFalse(self.license_original_pdf_url in response.context["licenses"])

    def test_license_list_succeding_release_title(self):
        response = self.client.get(
            self.license_list_url,
            {
                "permission_level": "",
                "license_title": "",
                "release_title": "Release_test",
            },
        )
        self.assertEquals(response.templates[0].name, "licenses/license_list.html")
        self.assertTrue(self.license_dummy in response.context["licenses"])

    def test_license_list_succeding_all_filter(self):
        response = self.client.get(
            self.license_list_url,
            {
                "permission_level": "RED",
                "license_title": "License_test",
                "release_title": "Release_test",
            },
        )
        self.assertTrue(self.license_dummy in response.context["licenses"])

    ###############################Delete Created Files, called after every test##############
    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
