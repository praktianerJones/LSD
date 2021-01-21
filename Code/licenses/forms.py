#SPDX-License-Identifier: BSD-3-Clause
'''
forms.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>

'''
from django import forms
from licenses.models import License


class LicensesRegisterForm(forms.ModelForm):
    """
    Form is used to add a license through an authenticated User.
    """

    class Meta:
        """
        Django Class, set the fields and other things your form shall display here.
        """
        model = License
        widgets = {"request_User": forms.HiddenInput()}
        fields = [
            "title",
            "permission_level_license",
            "annotation",
            "request_User",
            "originalText",
        ]
