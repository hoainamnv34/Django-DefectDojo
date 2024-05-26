# Generated by Django 4.1.13 on 2024-05-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0209_engevaluate_engagement_eng_evaluate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engevaluate',
            name='initial_points',
        ),
        migrations.AddField(
            model_name='engevaluate',
            name='threshold',
            field=models.IntegerField(blank=True, help_text='Threshold for the engagement', null=True, verbose_name='Threshold'),
        ),
    ]
