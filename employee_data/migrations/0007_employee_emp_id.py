# Generated by Django 5.0.1 on 2024-01-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data', '0006_remove_address_country_employee_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(default=True, unique=True),
        ),
    ]
