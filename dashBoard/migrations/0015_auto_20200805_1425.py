# Generated by Django 3.0.8 on 2020-08-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoard', '0014_auto_20200805_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='templatePath',
            field=models.FileField(blank=True, null=True, upload_to='qTemplate'),
        ),
    ]
