# Generated by Django 2.1.7 on 2020-10-22 12:55


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("licenses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Package",
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
                ("package_name", models.CharField(max_length=100)),
                ("package_version", models.CharField(max_length=50)),
                ("package_description", models.TextField(blank=True)),
                (
                    "usage",
                    models.CharField(
                        choices=[
                            ("d", "dynamic"),
                            ("s", "static"),
                            ("r", "rootfs"),
                            ("u", "unknown"),
                        ],
                        default="u",
                        max_length=1,
                    ),
                ),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "license_list",
                    models.ManyToManyField(
                        related_name="linked_licenses", to="licenses.License"
                    ),
                ),
                (
                    "license_used",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="licenses.License",
                    ),
                ),
                (
                    "package_creator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
