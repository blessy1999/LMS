# Generated by Django 5.0.1 on 2024-02-07 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_issuedbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='admno',
            new_name='enrollment',
        ),
    ]
