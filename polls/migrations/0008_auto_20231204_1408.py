# Generated by Django 3.2.5 on 2023-12-04 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_archive_result'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RangeYear',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
