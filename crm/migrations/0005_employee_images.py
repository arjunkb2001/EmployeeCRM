# Generated by Django 4.2.6 on 2023-11-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_remove_employee_contactno_employee_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='images',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
