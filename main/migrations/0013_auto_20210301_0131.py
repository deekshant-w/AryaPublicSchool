# Generated by Django 3.1.7 on 2021-02-28 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_admincontrols_redirecturl'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='information',
            new_name='news',
        ),
    ]