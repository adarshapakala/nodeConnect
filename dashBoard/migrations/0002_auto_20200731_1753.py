# Generated by Django 3.0.8 on 2020-07-31 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catogeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='questions',
            name='catogery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashBoard.Catogeries'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashBoard.Platforms'),
        ),
    ]