# Generated by Django 4.2 on 2023-05-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlematch',
            name='away_score',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='singlematch',
            name='home_score',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='teammatch',
            name='away_score',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='teammatch',
            name='home_score',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
