# Generated by Django 4.1 on 2022-08-14 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_name',
            new_name='user',
        ),
    ]
