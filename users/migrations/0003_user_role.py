# Generated by Django 4.2.7 on 2024-04-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_confirmation_code_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'member'), ('moderator', 'moderator'), ('admin', 'admin')], default='member', max_length=25, verbose_name='роль'),
        ),
    ]
