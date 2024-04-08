# Generated by Django 4.2.7 on 2024-04-06 14:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modules', '0005_module_liked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='liked_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_modules', to=settings.AUTH_USER_MODEL, verbose_name='лайкнувшие'),
        ),
    ]