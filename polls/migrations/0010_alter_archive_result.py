# Generated by Django 3.2.5 on 2023-12-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_archive_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='result',
            field=models.CharField(max_length=1000),
        ),
    ]
