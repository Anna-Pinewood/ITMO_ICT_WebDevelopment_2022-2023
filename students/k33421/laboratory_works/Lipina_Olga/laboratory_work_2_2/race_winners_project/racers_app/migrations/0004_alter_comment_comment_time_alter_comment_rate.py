# Generated by Django 4.1.2 on 2022-10-24 12:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("racers_app", "0003_comment_comment_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment_time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2022, 10, 24, 15, 18, 45, 232455)
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="rate",
            field=models.IntegerField(
                blank=True,
                default=10,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="Поставьте рейтинг",
            ),
        ),
    ]