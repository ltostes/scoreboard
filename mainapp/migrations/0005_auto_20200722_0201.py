# Generated by Django 3.0.2 on 2020-07-22 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_note_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='playoff_round',
            field=models.CharField(blank=True, choices=[('SF1', 'Semi-final 1'), ('SF2', 'Semi-final 2'), ('F', 'Final'), ('3', '3rd Place Dispute')], max_length=3, null=True),
        ),
    ]
