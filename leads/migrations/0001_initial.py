# Generated by Django 5.1.2 on 2024-10-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lead",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=40)),
                ("last_name", models.CharField(max_length=30)),
                ("age", models.IntegerField(default=0)),
            ],
        ),
    ]