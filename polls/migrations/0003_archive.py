# Generated by Django 3.2.5 on 2023-11-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20231115_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('result', models.TextField()),
            ],
        ),
    ]