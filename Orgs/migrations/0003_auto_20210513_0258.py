# Generated by Django 3.1.7 on 2021-05-13 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orgs', '0002_auto_20210512_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displayset',
            name='node_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display_sets', to='Orgs.nodetype'),
        ),
    ]