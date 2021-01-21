#SPDX-License-Identifier: BSD-3-Clause
'''
models.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>
'''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from licenses.models import License


class Package(models.Model):
    """
    A package represents a software package used by a software. It's main function
    is to represent external software and its license. 
    """
    PACKAGE_TYPE = {
        ('dynamic', 'dynamic'),
        ('static', 'static'),
        ('rootfs', 'rootfs'),
        ('unkown', 'unkown'),
    }

    package_name = models.CharField(max_length=100)
    package_version = models.CharField(max_length=50)
    package_description = models.TextField(blank=True)
    usage = models.CharField(max_length=1, choices=PACKAGE_TYPE, default="u")
    license_list = models.ManyToManyField(
        "licenses.License", related_name="linked_licenses"
    )
    license_used = models.ForeignKey(License, on_delete=models.PROTECT, null=False)
    date = models.DateTimeField(default=timezone.now)
    package_creator = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.package_name)
