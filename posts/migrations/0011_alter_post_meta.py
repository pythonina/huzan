# Generated by Django 4.1.2 on 2022-10-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='meta',
            field=models.CharField(max_length=255, verbose_name='تگ متا'),
        ),
    ]