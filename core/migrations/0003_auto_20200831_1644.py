# Generated by Django 3.1 on 2020-08-31 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200831_1636'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DownloadLinks',
            new_name='DownloadLink',
        ),
        migrations.RenameModel(
            old_name='WachLinks',
            new_name='WachLink',
        ),
    ]
