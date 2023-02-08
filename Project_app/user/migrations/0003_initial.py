# Generated by Django 4.1.5 on 2023-02-08 08:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0002_delete_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("created", models.DateTimeField(auto_created=True)),
                ("body", models.TextField(blank=True, null=True)),
                (
                    "value",
                    models.CharField(
                        choices=[("up", "Up Vote"), ("down", "Down Vote")],
                        max_length=200,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.projects"
                    ),
                ),
            ],
        ),
    ]
