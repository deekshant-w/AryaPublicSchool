# Generated by Django 3.1.7 on 2021-02-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminControls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionsOn', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('details', models.TextField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('displayDate', models.DateTimeField(blank=True, help_text='Used to sort the all informations')),
                ('archieve', models.BooleanField(default=False, help_text='Hides this information')),
                ('important', models.BooleanField(default=False, help_text='Signifies that this is important')),
            ],
        ),
        migrations.CreateModel(
            name='loadingModal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.TextField()),
                ('linkto', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('archieve', models.BooleanField(default=False, help_text='Hides this information')),
            ],
        ),
        migrations.CreateModel(
            name='newPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('file', models.FileField(blank=True, upload_to='')),
                ('image', models.ImageField(upload_to='')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('displayDate', models.DateTimeField(blank=True, help_text='Used to sort the all informations')),
                ('archieve', models.BooleanField(default=False, help_text='Hides this information')),
            ],
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('file', models.FileField(upload_to='')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('displayDate', models.DateTimeField(blank=True, help_text='Used to sort the all informations')),
                ('archieve', models.BooleanField(default=False, help_text='Hides this information')),
                ('important', models.BooleanField(default=False, help_text='Signifies that this is important')),
            ],
        ),
    ]