# Generated by Django 2.1.7 on 2020-07-21 16:36, Modified by SHentges


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lsd", "0006_auto_20200708_1629"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name="release",
                    name="status",
                    field=models.CharField(
                        choices=[("d", "Draft"), ("r", "Released"), ("w", "Withdrawn")],
                        default="d",
                        max_length=1,
                    ),
                ),
            ],
            database_operations=[],
        ),
    ]
