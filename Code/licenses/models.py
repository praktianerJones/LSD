#SPDX-License-Identifier: BSD-3-Clause
'''
models.py

(C) Copyright 2020 Friedrich Luetze GmbH, J. Luelsdorf <lsd@luetze.de>

'''

import datetime
from django.db import models
from django.contrib.auth.models import User

PERMISSION_LEVEL = ((0, "RED"), (1, "YELLOW"), (2, "GREEN"))


class Paragraph(models.Model):
    """
    This class has no functionality yet, it
    will be there to represent the Paragraph(s) of a Section.
    """
    permission_level = models.IntegerField(choices=PERMISSION_LEVEL, default="0")
    paragraph_text = models.TextField()


class Section(models.Model):
    """
    This class has no functionality yet, it
    will be there to represent the Section(s) of a License.
    """
    linked_paragraphs = models.ManyToManyField(
        "licenses.Paragraph", related_name="Section"
    )
    annotation = models.TextField()
    permission_level_section = models.IntegerField(
        choices=PERMISSION_LEVEL,
        auto_created=True,
        default=0,
    )


def license_file_directory_path(self):
    """
    Sets path of File.
    File will be uploaded to media/TextFileLicenses/<title>_timestamp .
    """
    if str(self.originalText).endswith(".pdf"):
        return "{0}{1}_{2}.pdf".format(
            "TextFileLicenses/", self.title, datetime.datetime.now()
        )
    return "{0}{1}_{2}.txt".format(
        "TextFileLicenses/", self.title, datetime.datetime.now()
    )


class License(models.Model):
    """
    A license represents the license of a software,
    in it the User of that software is informed what rights
    and obligations he has by using it.
    """

    title = models.CharField(max_length=100)
    linked_sections = models.ManyToManyField(
        "licenses.Section", related_name="License", blank=True
    )
    permission_level_license = models.IntegerField(
        choices=PERMISSION_LEVEL, auto_created=True, default=0
    )
    annotation = models.CharField(max_length=512)
    originalText = models.FileField(upload_to=license_file_directory_path)
    # Temporary Variable for Pull Request will be splited into three User
    # responsible User
    # creater
    # last edited
    request_User = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    # additional Field Status so the License gets double checked before beeing active

    def __str__(self):
        return str(self.title)
