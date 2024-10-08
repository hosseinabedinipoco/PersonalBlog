# Generated by Django 5.1 on 2024-09-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_content'),
        ('users', '0003_remove_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='view_user',
            field=models.ManyToManyField(null=True, related_name='articles_viewed', to='users.user'),
        ),
    ]
