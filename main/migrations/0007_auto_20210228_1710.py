# Generated by Django 3.1.7 on 2021-02-28 11:40

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210228_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loadingmodal',
            name='html',
        ),
        migrations.AddField(
            model_name='loadingmodal',
            name='data',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loadingmodal',
            name='linkto',
            field=models.CharField(max_length=1024),
        ),
    ]
