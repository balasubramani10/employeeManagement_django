# Generated by Django 5.0.1 on 2024-01-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data', '0008_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(default=0),
        ),
    ]
