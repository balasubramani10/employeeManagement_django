# Generated by Django 5.0.1 on 2024-01-17 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='location',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='branch_address',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_adress', to='office_data.branch'),
        ),
    ]
