#SPDX-License-Identifier: BSD-3-Clause
'''
test_forms.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
from django.test import TestCase
from licenses.forms import LicensesRegisterForm


class MyTest(TestCase):
    def test_forms(self):
        form_data = {
            "title": "License_test",
            "permission_level_license": "0",
            "annotation": "gibet nicht",
            "request_User": "TestUser",
            "originalText": "tests/License_test.txt",
        }
        form = LicensesRegisterForm(data=form_data)
        self.assertTrue(form.is_valid)
