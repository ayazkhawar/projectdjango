# Generated by Django 3.1.8 on 2022-07-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employee_mobile',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='emplyee_regNo',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_address',
            field=models.TextField(null=True),
        ),
    ]
