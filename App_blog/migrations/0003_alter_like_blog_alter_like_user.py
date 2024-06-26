# Generated by Django 5.0.6 on 2024-06-24 04:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_blog', '0002_alter_blog_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_blog', to='App_blog.blog'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
