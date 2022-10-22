# Generated by Django 4.1.2 on 2022-10-19 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("project_first_app", "0003_alter_owner_date_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auto",
            name="color",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="owning",
            name="auto_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="project_first_app.auto",
            ),
        ),
        migrations.AlterField(
            model_name="owning",
            name="date_end",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="owning",
            name="owner_auto",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="project_first_app.owner",
            ),
        ),
    ]