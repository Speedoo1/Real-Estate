# Generated by Django 3.2.9 on 2022-11-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_amenities_propertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertise',
            name='bathroom',
            field=models.IntegerField(null=True),
        ),
    ]
