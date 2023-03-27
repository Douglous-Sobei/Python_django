# Generated by Django 4.1.7 on 2023-02-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teams",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("desgination", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="images/%Y/%m/%d")),
                ("facebook_link", models.URLField(max_length=95)),
                ("twiter_link", models.URLField(max_length=80)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
