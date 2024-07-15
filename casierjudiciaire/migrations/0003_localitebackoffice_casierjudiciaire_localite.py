# Generated by Django 4.1.7 on 2024-07-02 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("casierjudiciaire", "0002_alter_casierjudiciaire_etat_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocaliteBackOffice",
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
                ("nom_province", models.CharField(max_length=255)),
                ("ville", models.CharField(max_length=255)),
                ("backend_api_gateway", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="casierjudiciaire",
            name="localite",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="casierjudiciaire.localitebackoffice",
            ),
        ),
    ]
