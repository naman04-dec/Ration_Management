# Generated by Django 3.2.6 on 2021-10-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('govApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='govration',
            name='aadhar_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='govration',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
