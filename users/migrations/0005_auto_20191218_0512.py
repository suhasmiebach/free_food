# Generated by Django 2.2.3 on 2019-12-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191217_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='latitude',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='food',
            name='longitude',
            field=models.CharField(max_length=18),
        ),
    ]