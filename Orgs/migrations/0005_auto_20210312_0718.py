# Generated by Django 3.1.7 on 2021-03-12 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orgs', '0004_auto_20210312_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Orgs.org'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Orgs.positionname'),
        ),
    ]
