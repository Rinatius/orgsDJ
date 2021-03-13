# Generated by Django 3.1.7 on 2021-03-12 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orgs', '0009_auto_20210312_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='employment',
            name='end_day',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='employment',
            name='end_month',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='employment',
            name='end_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)]),
        ),
        migrations.AddField(
            model_name='employment',
            name='start_day',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='employment',
            name='start_month',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
    ]
