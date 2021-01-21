#SPDX-License-Identifier: BSD-3-Clause


'''
test_models.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf@luetze.de
'''
from django.test import TestCase
from packages.models import Package
from licenses.models import License
from django.contrib.auth.models import User


class TestModels(TestCase):
    """
    Every Model from the App Package is tested here.
    First the database is setUp.
    Afterwards it will be checked if the database is filled with the model and the connection
    between different models are implemented through django
    """

    def setUp(self):
        # package/license Creator
        self.test_User = User.objects.create_user(
            username="user1", email="user@mail.com", password="test"
        )
        # license
        self.test_license = License.objects.create(
            annotation="Dies ist ein Kommentar, es mag aussehen wie ein Lückenfüller, doch es hat Herz.",
            originalText="Der Originale Text der Lizenz wird sich hier befinden.",
            request_User=self.test_User,
            permission_level_license=1,
        )
        # package
        self.test_package = Package.objects.create(
            package_name="package1",
            package_version="V1",
            package_description="Nice package",
            usage="u",
            license_used=self.test_license,
            package_creator=self.test_User,
        )
        self.test_package.license_list.add(self.test_license)

    def test_package_in_Database(self):
        self.assertEquals(Package.objects.get(pk=1), self.test_package)

    def test_package_license_conncection(self):
        self.assertEquals(Package.objects.get(pk=1).license_used, self.test_license)
        self.assertEquals(
            Package.objects.get(pk=1).license_list.first(), self.test_license
        )

    def test_package_user_connection(self):
        self.assertEquals(Package.objects.get(pk=1).package_creator, self.test_User)
