# Generated by Django 5.0.4 on 2024-05-07 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("descipcion", models.TextField()),
                ("imagen", models.ImageField(upload_to="blog/images")),
                ("date", models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]