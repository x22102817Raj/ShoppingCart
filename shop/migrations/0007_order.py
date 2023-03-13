# Generated by Django 4.1.7 on 2023-03-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_favourite"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("email", models.EmailField(max_length=254)),
                ("paid", models.BooleanField(default="False")),
                ("amount", models.IntegerField(default=0)),
                ("description", models.CharField(default=None, max_length=800)),
            ],
        ),
    ]
