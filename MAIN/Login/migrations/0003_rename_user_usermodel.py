# Generated by Django 5.1.4 on 2025-01-07 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_rename_name_user_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserModel',
        ),
    ]