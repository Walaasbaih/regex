# Generated by Django 3.0.5 on 2020-10-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myreg', '0003_auto_20201029_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.CharField(default='null', max_length=200)),
                ('expression', models.CharField(max_length=500)),
            ],
        ),
    ]