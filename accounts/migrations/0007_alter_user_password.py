# Generated by Django 4.1.2 on 2023-12-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]