# Generated by Django 4.1.1 on 2022-10-13 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'ویژگی', 'verbose_name_plural': 'ویژگی ها'},
        ),
        migrations.AlterModelOptions(
            name='propertyvalue',
            options={'verbose_name': 'مقدار ویژگی', 'verbose_name_plural': 'مقادیر ویژگی ها'},
        ),
    ]