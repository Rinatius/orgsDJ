# Generated by Django 3.1.7 on 2021-05-13 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orgs', '0004_displayset_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edgetype',
            old_name='additional_schema',
            new_name='json_schema',
        ),
        migrations.RenameField(
            model_name='nodetype',
            old_name='additional_schema',
            new_name='json_schema',
        ),
    ]