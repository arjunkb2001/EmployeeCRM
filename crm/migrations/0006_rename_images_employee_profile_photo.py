# Generated by Django 4.2.6 on 2023-11-09 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_employee_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='images',
            new_name='profile_photo',
        ),
    ]