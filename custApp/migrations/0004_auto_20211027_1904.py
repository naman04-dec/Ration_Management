# Generated by Django 3.0.11 on 2021-10-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custApp', '0003_alter_custration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custration',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
