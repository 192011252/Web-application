# Generated by Django 4.0.7 on 2023-09-13 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_creator', '0015_template_images_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='creator_table',
        ),
        migrations.DeleteModel(
            name='Magazine',
        ),
    ]
