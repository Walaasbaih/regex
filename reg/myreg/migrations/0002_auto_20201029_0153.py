# Generated by Django 3.0.5 on 2020-10-28 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myreg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='input1',
            field=models.CharField(max_length=30, verbose_name='input1'),
        ),
    ]
