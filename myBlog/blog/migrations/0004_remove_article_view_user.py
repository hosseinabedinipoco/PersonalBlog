# Generated by Django 5.1 on 2024-09-06 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_view_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='view_user',
        ),
    ]
