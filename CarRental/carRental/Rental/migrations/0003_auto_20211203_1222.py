# Generated by Django 3.2.9 on 2021-12-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0002_auto_20211203_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_mpg',
            new_name='car_mpg1',
        ),
        migrations.AddField(
            model_name='car',
            name='car_mpg2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]