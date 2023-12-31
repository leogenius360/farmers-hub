# Generated by Django 4.2 on 2023-07-04 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.auth_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("farm", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmanagement",
            name="created_by",
            field=models.ForeignKey(
                default=utils.auth_utils.get_anonymous_user,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="user_created_product_mgt",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created by",
            ),
        ),
        migrations.AddField(
            model_name="farmproduct",
            name="adapted_mgt",
            field=models.ManyToManyField(
                related_name="product_adapted_mgt",
                to="farm.farmmanagement",
                verbose_name="Adapted managements/plans",
            ),
        ),
        migrations.AddField(
            model_name="farmproduct",
            name="custom_mgt",
            field=models.ManyToManyField(
                related_name="product_custom_mgt",
                to="farm.farmmanagement",
                verbose_name="Custom managements/plans",
            ),
        ),
        migrations.AddField(
            model_name="farmproduct",
            name="farm",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="farm_products",
                to="farm.farm",
                verbose_name="Farm",
            ),
        ),
        migrations.AddField(
            model_name="farmmanagement",
            name="created_by",
            field=models.ForeignKey(
                default=utils.auth_utils.get_anonymous_user,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="user_created_farm_mgt",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created by",
            ),
        ),
        migrations.AddField(
            model_name="farm",
            name="adapted_mgt",
            field=models.ManyToManyField(
                related_name="farm_adapted_mgt",
                to="farm.farmmanagement",
                verbose_name="Adapted managements/plans",
            ),
        ),
        migrations.AddField(
            model_name="farm",
            name="custom_mgt",
            field=models.ManyToManyField(
                related_name="farm_custom_mgt",
                to="farm.farmmanagement",
                verbose_name="Custom managements/plans",
            ),
        ),
        migrations.AddField(
            model_name="farm",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_farms",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Farm owner",
            ),
        ),
    ]
