# Generated by Django 3.2.6 on 2021-08-17 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tiitle',
            new_name='title',
        ),
    ]
