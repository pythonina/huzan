# Generated by Django 4.1.1 on 2022-10-13 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_property_options_alter_propertyvalue_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'تگ', 'verbose_name_plural': 'تگ ها'},
        ),
    ]