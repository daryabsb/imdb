# Generated by Django 3.1 on 2020-09-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200902_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('arabic', 'ARABIC'), ('kurdish', 'KURDISH'), ('germany', 'GERMAN')], max_length=15),
        ),
    ]