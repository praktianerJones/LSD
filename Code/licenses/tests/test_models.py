#SPDX-License-Identifier: BSD-3-Clause
'''
test_models.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
from django.test import TestCase
from licenses.models import Paragraph, Section, License, User


class TestModels(TestCase):
    """
    Every Model from the App licenses is tested in here.
    First the database is setUp.
    It will be checked if the database is filled with the model and the connections
    between different models are implemented through django
    """

    def setUp(self):
        """
        put license into the database and fill it with a User and a license
        """
        self.test_User = User.objects.create_user(
            username="user1", email="user@mail.com", password="test"
        )
        self.test_fail_User = User.objects.create_user(
            username="user2", email="user@mail.com", password="test"
        )
        self.test_license = License.objects.create(
            annotation="Dies ist ein Kommentar, es mag aussehen wie ein Lückenfüller, doch es hat Herz.",
            originalText="Der Originale Text der Lizenz wird sich hier befinden.",
            request_User=self.test_User,
            permission_level_license=1,
        )
        self.test_fail_license = License.objects.create(
            annotation="I am so excited.",
            originalText="And I just can't hide it...",
            request_User=self.test_User,
            permission_level_license=1,
        )

    ###############################succeding Tests################################################

    def test_license_is_in_Database(self):
        self.assertEquals(License.objects.get(pk=1), self.test_license)
        self.assertEquals(
            License.objects.get(pk=1).annotation,
            "Dies ist ein Kommentar, es mag aussehen wie ein Lückenfüller, doch es hat Herz.",
        )
        self.assertEquals(
            License.objects.get(pk=1).originalText,
            "Der Originale Text der Lizenz wird sich hier befinden.",
        )

    def test_License_is_assigned_to_User(self):
        self.assertEquals(License.objects.get(pk=1).request_User, self.test_User)

    ###############################failling Tests##################################################

    def test_fail_license_is_in_Database(self):
        self.assertNotEquals(License.objects.get(pk=2), self.test_license)

    def test_fail_License_is_assigned_to_User(self):
        self.assertNotEquals(
            License.objects.get(pk=1).request_User, self.test_fail_User
        )
