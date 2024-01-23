# Generated by Django 5.0.1 on 2024-01-17 19:08

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('u_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.IntegerField()),
                ('contact_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Branch_Address',
            fields=[
                ('u_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('line1', models.CharField(max_length=64)),
                ('line2', models.CharField(blank=True, max_length=64, null=True)),
                ('land_mark', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(max_length=64)),
                ('pincode', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_data.branch')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]