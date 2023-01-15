# Generated by Django 4.1.3 on 2022-11-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="rating",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, 0),
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                ],
                default=None,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="plannedconference",
            name="themes",
            field=models.ManyToManyField(to="conferences.theme"),
        ),
        migrations.AddField(
            model_name="registeredconference",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="registeredconference",
            name="results",
            field=models.CharField(
                blank=True,
                choices=[(1, "Рекомендован"), (2, "Не рекомендован")],
                max_length=50,
                null=True,
            ),
        ),
    ]