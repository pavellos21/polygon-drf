# Generated by Django 4.1.3 on 2022-12-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polygon", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="servicearea",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]