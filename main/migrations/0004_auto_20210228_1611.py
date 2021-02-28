# Generated by Django 3.1.7 on 2021-02-28 10:41

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210228_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpage',
            name='file',
        ),
        migrations.AddField(
            model_name='newpage',
            name='details',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='information',
            name='details',
            field=tinymce.models.HTMLField(),
        ),
    ]