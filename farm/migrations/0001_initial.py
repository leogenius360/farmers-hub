# Generated by Django 4.2 on 2023-07-04 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Farm",
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
                ("slug", models.SlugField(editable=False, verbose_name="In-app url")),
                ("name", models.CharField(max_length=120, verbose_name="Name")),
                (
                    "short_desc",
                    models.CharField(max_length=250, verbose_name="Short description"),
                ),
                (
                    "long_desc",
                    models.CharField(max_length=1024, verbose_name="Long description"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="created on"
                    ),
                ),
                (
                    "last_modified",
                    models.DateTimeField(auto_now=True, verbose_name="last modified"),
                ),
            ],
            options={
                "verbose_name": "Farm",
                "verbose_name_plural": "Farms",
            },
        ),
        migrations.CreateModel(
            name="FarmManagement",
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
                ("slug", models.SlugField(editable=False, verbose_name="In-app url")),
                ("name", models.CharField(max_length=120, verbose_name="Name")),
                (
                    "short_desc",
                    models.CharField(max_length=250, verbose_name="Short description"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="created on"
                    ),
                ),
                (
                    "last_modified",
                    models.DateTimeField(auto_now=True, verbose_name="last modified"),
                ),
                ("long_desc", models.TextField(verbose_name="Long description")),
            ],
            options={
                "verbose_name": "Farm management",
                "verbose_name_plural": "Farm managements",
            },
        ),
        migrations.CreateModel(
            name="FarmProduct",
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
                ("slug", models.SlugField(editable=False, verbose_name="In-app url")),
                ("name", models.CharField(max_length=120, verbose_name="Name")),
                (
                    "short_desc",
                    models.CharField(max_length=250, verbose_name="Short description"),
                ),
                (
                    "long_desc",
                    models.CharField(max_length=1024, verbose_name="Long description"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="created on"
                    ),
                ),
                (
                    "last_modified",
                    models.DateTimeField(auto_now=True, verbose_name="last modified"),
                ),
            ],
            options={
                "verbose_name": "Farm product",
                "verbose_name_plural": "Farm products",
            },
        ),
        migrations.CreateModel(
            name="ProductManagement",
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
                ("slug", models.SlugField(editable=False, verbose_name="In-app url")),
                ("name", models.CharField(max_length=120, verbose_name="Name")),
                (
                    "short_desc",
                    models.CharField(max_length=250, verbose_name="Short description"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="created on"
                    ),
                ),
                (
                    "last_modified",
                    models.DateTimeField(auto_now=True, verbose_name="last modified"),
                ),
                ("long_desc", models.TextField(verbose_name="Long description")),
            ],
            options={
                "verbose_name": "Product management",
                "verbose_name_plural": "Product managements",
            },
        ),
    ]