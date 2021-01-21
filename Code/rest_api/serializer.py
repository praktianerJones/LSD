#SPDX-License-Identifier: BSD-3-Clause
'''
serializer.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges, J. Luelsdorf <lsd@luetze.de>

'''
from rest_framework import serializers
from software.models import Release
from products.models import Product
from licenses.models import License
from packages.models import Package


class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer, if required is not explicitly set to False it is implicitly required
    """
    class Meta:
        model = Product
        fields = "__all__"
        # It has to be defined if Products / Familys / Software has to be created first.
        # Currently it is possible to create a Product
        #  without a link to its family or Linked software.
        extra_kwargs = {
            "id": {"read_only": True},
            "article_number": {"allow_blank": False},
            "article_description": {"allow_blank": False, "required": False},
            "linked_software": {"required": False},
            "families": {"required": False},
            "content": {"allow_blank": False, "required": False},
            "date_posted": {"read_only": True},
        }


class LicenseSerializer(serializers.ModelSerializer):
    """
    License Serializer
    """
    class Meta:
        model = License
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "linked_sections": {"required": False},
        }


class PackageSerializer(serializers.ModelSerializer):
    """
    Package Serializer
    """
    # SlugRelatedField lets the User file in the JsonForm with a -> slug_field
    license_list = serializers.SlugRelatedField(
        many=True, queryset=License.objects.all(), slug_field="title"
    )
    license_used = serializers.SlugRelatedField(
        slug_field="title", queryset=License.objects.all()
    )

    class Meta:
        model = Package
        fields = [
            "id",
            "package_name",
            "package_version",
            "package_description",
            "usage",
            "date",
            "package_creator",
            "license_list",
            "license_used",
        ]
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
            "license_list": {"required": False},
            "package_creator": {"required": False},
        }


class ReleaseSerializer(serializers.ModelSerializer):
    """
    Release Serializer
    """
    linked_packages = PackageSerializer(many=True, read_only=True)
    linked_licenses = LicenseSerializer(many=True, read_only=True)

    class Meta:
        model = Release
        fields = [
            "id",
            "title",
            "version_string",
            "version_major",
            "version_minor",
            "version_micro",
            "version_build",
            "version_commit",
            "git_path",
            "bin_path",
            "doc_path_html",
            "doc_path_pdf",
            "date",
            "laste_edited_by",
            "linked_packages",
            "linked_licenses",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "title": {"allow_blank": False, "required": False},
            "version_string": {"required": False},
            "version_commit": {"allow_blank": False, "required": False},
            "git_path": {"allow_blank": False, "required": False},
            "bin_path": {"allow_blank": False, "required": False},
            "doc_path_html": {"allow_blank": False, "required": False},
            "doc_path_pdf": {"allow_blank": False, "required": False},
            "date": {"required": False},
            "linked_licenses": {"required": False},
            "linked_packages": {"required": False},
        }
