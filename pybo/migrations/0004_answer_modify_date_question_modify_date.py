# Generated by Django 4.1.3 on 2022-12-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pybo", "0003_answer_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]