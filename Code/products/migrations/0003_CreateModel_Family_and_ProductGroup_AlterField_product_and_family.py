# Generated by Django 2.1.7 on 2020-07-29 06:24
# modified by J. Luelsdorf


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0002_AlterField_linked_software_to_softwareRelease"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Family",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("title", models.CharField(max_length=100)),
                        ("description", models.TextField()),
                        (
                            "date",
                            models.DateTimeField(default=django.utils.timezone.now),
                        ),
                        (
                            "laste_edited_by",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.PROTECT,
                                to=settings.AUTH_USER_MODEL,
                            ),
                        ),
                    ],
                ),
                migrations.CreateModel(
                    name="ProductGroup",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("title", models.CharField(max_length=100)),
                        ("description", models.TextField()),
                        (
                            "date",
                            models.DateTimeField(default=django.utils.timezone.now),
                        ),
                        (
                            "laste_edited_by",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.PROTECT,
                                to=settings.AUTH_USER_MODEL,
                            ),
                        ),
                    ],
                ),
                migrations.AlterField(
                    model_name="product",
                    name="families",
                    field=models.ManyToManyField(
                        related_name="families", to="products.Family"
                    ),
                ),
                migrations.AddField(
                    model_name="family",
                    name="product_groups",
                    field=models.ManyToManyField(
                        related_name="product_groups", to="products.ProductGroup"
                    ),
                ),
            ],
            database_operations=[],
        )
    ]