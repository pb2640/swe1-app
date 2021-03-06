# Generated by Django 4.0.1 on 2022-01-10 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="choice_text",
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name="choice",
            name="question",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.question",
            ),
        ),
        migrations.AddField(
            model_name="choice",
            name="votes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(null=True, verbose_name="date published"),
        ),
        migrations.AddField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
