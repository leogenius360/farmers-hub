# Generated by Django 4.2 on 2023-07-04 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("long_desc", models.TextField(verbose_name="Long description")),
                (
                    "img",
                    models.ImageField(
                        upload_to="market/product_imgs", verbose_name="Image"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=7,
                        verbose_name="Price",
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=5,
                        verbose_name="Discount",
                    ),
                ),
                (
                    "target",
                    models.CharField(
                        choices=[
                            ("all", "ALL"),
                            ("us", "MARKET USERS"),
                            ("fm", "FARMERS ONLY"),
                            ("agro", "AGRO-SERVICES ONLY"),
                            ("sup", "SUPPORT ONLY"),
                        ],
                        default=("us", "MARKET USERS"),
                        max_length=120,
                        verbose_name="Market target",
                    ),
                ),
                ("qty", models.IntegerField(default=0, verbose_name="Quantity")),
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
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Sale",
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
                ("slug", models.SlugField(unique=True, verbose_name="In-app url")),
                (
                    "payment",
                    models.CharField(
                        choices=[
                            ("pending", "PENDING"),
                            ("part_30", "PAID (30%)"),
                            ("part_50", "PAID (50%)"),
                            ("part_80", "PAID (80%)"),
                            ("full", "FULL PAYMENT"),
                        ],
                        default=("pending", "PENDING"),
                        max_length=120,
                        verbose_name="Payment",
                    ),
                ),
                (
                    "delivery",
                    models.CharField(
                        choices=[("pending", "PENDING"), ("delivered", "DELIVERED")],
                        default=("pending", "PENDING"),
                        max_length=120,
                        verbose_name="Delivery",
                    ),
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
                "verbose_name": "Sales",
                "verbose_name_plural": "Sales",
            },
        ),
        migrations.CreateModel(
            name="Store",
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
                ("long_desc", models.TextField(verbose_name="Long description")),
                (
                    "img",
                    models.ImageField(
                        upload_to="market/product_imgs", verbose_name="Image"
                    ),
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
                "verbose_name": "Store",
                "verbose_name_plural": "Stores",
            },
        ),
    ]
