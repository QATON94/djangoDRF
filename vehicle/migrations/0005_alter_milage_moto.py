# Generated by Django 5.0.6 on 2024-06-08 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_alter_milage_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milage',
            name='moto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milage', to='vehicle.moto'),
        ),
    ]
