# Generated by Django 4.0.7 on 2023-09-02 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_creator', '0002_creator_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='creator_details',
        ),
    ]
