#SPDX-License-Identifier: BSD-3-Clause
'''
models.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Hentges, J. Luelsdorf <lsd@luetze.de>
'''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    """
    A Product represents a finished product of the company.
    """
    title = models.CharField(max_length=100)
    article_number = models.CharField(max_length=100)
    article_revision = models.IntegerField()
    article_description = models.TextField()
    families = models.ManyToManyField("products.Family", related_name="families")
    linked_software = models.ManyToManyField(
        "software.Release", related_name="releases"
    )
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.title)


class ProductGroup(models.Model):
    """
    A ProductGroup is a Cluster of Families.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    laste_edited_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.title)


class Family(models.Model):
    """
    A Family is a Cluster of Products.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    product_groups = models.ManyToManyField(
        "ProductGroup", related_name="product_groups"
    )
    date = models.DateTimeField(default=timezone.now)
    laste_edited_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.title)
