# Generated by Django 4.2.6 on 2023-10-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_remove_employee_contact_employee_contactno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='contactno',
        ),
        migrations.AddField(
            model_name='employee',
            name='contact',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
