# Generated by Django 4.0.3 on 2022-03-10 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotoportal1', '0003_alter_pkmn_bigimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='season',
            field=models.IntegerField(default='816', null=True, validators=[django.core.validators.MinValueValidator(810), django.core.validators.MaxValueValidator(1099)]),
        ),
    ]