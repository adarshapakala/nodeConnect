# Generated by Django 3.0.8 on 2020-08-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoard', '0009_auto_20200805_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='templatePath',
            field=models.FilePathField(default='C:\\Pills\\LabVIEW\\General\x01\x01.vi', path='template'),
            preserve_default=False,
        ),
    ]
