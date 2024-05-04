# Generated by Django 5.0.4 on 2024-04-24 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0001_initial"),
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="perk",
            name="detatils",
        ),
        migrations.AddField(
            model_name="experience",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
        migrations.AddField(
            model_name="perk",
            name="details",
            field=models.CharField(blank=True, default=" ", max_length=250),
        ),
        migrations.AlterField(
            model_name="perk",
            name="explanation",
            field=models.TextField(blank=True, default=" "),
        ),
    ]
