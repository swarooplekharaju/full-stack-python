# Generated by Django 3.1.2 on 2020-10-10 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='vaccination',
            new_name='vaccinations',
        ),
    ]