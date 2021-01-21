#SPDX-License-Identifier: BSD-3-Clause
'''
forms.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
from django import forms
from software.models import Release


class ReleaseAddLicenseForm(forms.ModelForm):
    """
    Form, used to add or change the License a software
    release uses.
    """
    class Meta:
        model = Release
        fields = ["linked_licenses"]
