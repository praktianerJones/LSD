#SPDX-License-Identifier: BSD-3-Clause
'''
models.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges <lsd@luetze.de>
'''
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tool(models.Model):
    """
    The Tool class represents the Tools used by the LSD.
    This can be variyng.
    """
    USAGE_STATUS = (
        ("a", "Approved"),
        ("l", "locked"),
    )

    SIL_LEVEL = (
        (0, "Basic Integrity"),
        (1, "SIL1"),
        (2, "SIL2"),
    )

    CLASSIFICATION = (
        (1, "T1"),
        (2, "T2"),
        (3, "T3"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    version = models.CharField(max_length=100)
    usage_status = models.CharField(max_length=1, choices=USAGE_STATUS, default="l")
    release_status = models.IntegerField(choices=SIL_LEVEL, default=0)
    responsible_user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="responsible_user_tool", null=True
    )
    proxy_user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="proxy_user", null=True
    )
    comment = models.TextField()
    system_requirements = models.TextField()
    license_model = models.TextField()
    license_host_path = models.CharField(max_length=512)
    classification = models.IntegerField(choices=CLASSIFICATION, null=True)
    specification_path = models.CharField(max_length=512)
    manual_path = models.CharField(max_length=512)
    proof_of_compliance_path = models.CharField(max_length=512)
    characterization_path = models.CharField(max_length=512)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
