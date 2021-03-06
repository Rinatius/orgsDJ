# Generated by Django 3.1.7 on 2021-03-14 04:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orgs', '0014_auto_20210313_0703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='additional_info',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='additional_info',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='end_day',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='end_month',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='start_day',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='start_month',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='start_year',
        ),
        migrations.RemoveField(
            model_name='org',
            name='part_of',
        ),
        migrations.AddField(
            model_name='org',
            name='predecessor_orgs',
            field=models.ManyToManyField(blank=True, null=True, related_name='_org_predecessor_orgs_+', to='Orgs.Org'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='second_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='positionname',
            name='name',
            field=models.CharField(max_length=400),
        ),
        migrations.CreateModel(
            name='PositionOrgHierarchyRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('start_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)])),
                ('start_month', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('start_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('end_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)])),
                ('end_month', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('end_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('subordinate_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orgs.org')),
                ('superior_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orgs.position')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgsStructuralRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('start_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)])),
                ('start_month', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('start_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('end_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)])),
                ('end_month', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('end_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('external_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_org', to='Orgs.org')),
                ('internal_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internal_org', to='Orgs.org')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgsHierarchyRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('start_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)])),
                ('start_month', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('start_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('end_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)])),
                ('end_month', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('end_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('subordinate_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subordinate_org', to='Orgs.org')),
                ('superior_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='superior_org', to='Orgs.org')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
