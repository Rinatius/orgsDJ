# Generated by Django 3.1.7 on 2021-03-14 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orgs', '0015_auto_20210314_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='predecessor_orgs',
            field=models.ManyToManyField(related_name='_org_predecessor_orgs_+', to='Orgs.Org'),
        ),
    ]
