# Generated by Django 4.1.5 on 2023-02-06 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]