# Generated by Django 4.1.2 on 2022-10-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_desc_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meta',
            field=models.CharField(default='', max_length=255, verbose_name='تگ متا'),
        ),
    ]
