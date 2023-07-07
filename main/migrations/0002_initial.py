# Generated by Django 4.2 on 2023-07-04 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.auth_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="store",
            name="owner",
            field=models.ForeignKey(
                default=utils.auth_utils.get_anonymous_user,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="stores",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Store owner",
            ),
        ),
        migrations.AddField(
            model_name="sale",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sales",
                to="main.product",
                verbose_name="Product",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="created_by",
            field=models.ForeignKey(
                default=utils.auth_utils.get_anonymous_user,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="market_products",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created by",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="store_products",
                to="main.store",
                verbose_name="Store",
            ),
        ),
    ]
