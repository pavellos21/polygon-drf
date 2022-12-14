# Generated by Django 4.1.3 on 2022-12-04 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polygon", "0003_alter_provider_deleted_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicearea",
            name="provider",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="service_areas",
                related_query_name="ice_area",
                to="polygon.provider",
            ),
            preserve_default=False,
        ),
    ]
