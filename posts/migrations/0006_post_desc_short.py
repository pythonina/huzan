# Generated by Django 4.1.2 on 2022-10-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_news_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc_short',
            field=models.CharField(default='', max_length=50, verbose_name='توضیحات کوتاه'),
        ),
    ]
