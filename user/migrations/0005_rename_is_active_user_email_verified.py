# Generated by Django 4.1.7 on 2023-05-10 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_active',
            new_name='email_verified',
        ),
    ]
