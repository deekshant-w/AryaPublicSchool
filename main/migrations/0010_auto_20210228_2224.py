# Generated by Django 3.1.7 on 2021-02-28 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_newpage_vertival'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newpage',
            old_name='vertival',
            new_name='vertical',
        ),
    ]
