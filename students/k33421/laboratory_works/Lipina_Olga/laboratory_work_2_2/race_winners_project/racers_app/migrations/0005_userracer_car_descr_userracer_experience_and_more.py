# Generated by Django 4.1.2 on 2022-10-24 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("racers_app", "0004_alter_comment_comment_time_alter_comment_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="userracer",
            name="car_descr",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userracer",
            name="experience",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userracer",
            name="fathername",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="userracer",
            name="team_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="userracer",
            name="type_user",
            field=models.CharField(
                choices=[("A", "Высший"), ("B", "Высокий"), ("C", "Иное")],
                default="C",
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name="userracer",
            name="user_descr",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="comment_time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2022, 10, 24, 16, 2, 5, 625467)
            ),
        ),
    ]