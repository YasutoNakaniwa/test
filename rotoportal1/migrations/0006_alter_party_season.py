# Generated by Django 4.0.3 on 2022-03-10 15:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotoportal1', '0005_alter_party_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='season',
            field=models.IntegerField(default='', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
