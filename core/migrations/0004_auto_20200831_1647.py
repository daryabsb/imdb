# Generated by Django 3.1 on 2020-08-31 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200831_1644'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DownloadLink',
            new_name='MovieLink',
        ),
        migrations.DeleteModel(
            name='WachLink',
        ),
    ]
