#SPDX-License-Identifier: BSD-3-Clause
'''
models.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges, J. Luelsdorf <lsd@luetze.de>

'''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Release(models.Model):
    """
    A Release represents Software which is developed by the Company.
    Every Release has different Users, which fill in different Roles.
    """
    STATUS_CODES = (
        ("d", "Draft"),
        ("r", "Released"),
        ("w", "Withdrawn"),
    )

    SIL_LEVEL = (
        (0, "Basic Integrity"),
        (1, "SIL1"),
        (2, "SIL2"),
    )

    SOFTWARE_TYPE = (
        ("i", "Internal"),
        ("e", "External"),
        ("t", "Third Party"),
    )

    title = models.CharField(max_length=100)
    version_string = models.TextField()
    version_major = models.IntegerField()
    version_minor = models.IntegerField()
    version_micro = models.IntegerField()
    version_build = models.IntegerField()
    version_commit = models.CharField(max_length=100)
    git_path = models.CharField(max_length=512)
    bin_path = models.CharField(max_length=512)
    doc_path_html = models.CharField(max_length=512)
    doc_path_pdf = models.CharField(max_length=512)
    date = models.DateTimeField(default=timezone.now)
    laste_edited_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="last_edit_user", null=True
    )
    status = models.CharField(max_length=1, choices=STATUS_CODES, default="d")
    sil_level = models.IntegerField(choices=SIL_LEVEL, default="0")
    developer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="developer_user", null=True
    )
    tester = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="tester_user", null=True
    )
    verifier = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="verifier_user", null=True
    )
    process_version = models.ForeignKey(
        "self", on_delete=models.PROTECT, related_name="using_releases", null=True
    )
    software_type = models.CharField(max_length=1, choices=SOFTWARE_TYPE, default="i")
    responsible_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="responsible_user_release",
        null=True,
    )
    linked_tools = models.ManyToManyField("tools.Tool", related_name="releases")
    linked_licenses = models.ManyToManyField(
        "licenses.License", related_name="licenses", blank=True
    )
    linked_packages = models.ManyToManyField(
        "packages.Package", related_name="package", blank=True
    )

    def __str__(self):
        return str(self.title)


    def get_url_list(self):
        """
        ToDo delete this function or add Description.
        """
        return "/software/{}".format(self.title)

    def get_url_details(self):
        """
        ToDo delete this function or add Description.
        """
        return "/software/{}/{}".format(self.title, self.version_string)
