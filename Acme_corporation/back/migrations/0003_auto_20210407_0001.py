# Generated by Django 3.1.7 on 2021-04-07 05:01

import back.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_auto_20210406_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intermediario',
            name='Dueno',
            field=models.CharField(db_column='Dueño', default=back.models.Carros, max_length=200),
        ),
    ]
