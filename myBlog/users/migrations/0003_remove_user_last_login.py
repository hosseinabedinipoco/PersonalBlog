# Generated by Django 5.1 on 2024-09-06 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]