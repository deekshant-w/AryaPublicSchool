# Generated by Django 3.1.7 on 2021-02-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_admincontrols_homepagetext'),
    ]

    operations = [
        migrations.AddField(
            model_name='admincontrols',
            name='redirectUrl',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]