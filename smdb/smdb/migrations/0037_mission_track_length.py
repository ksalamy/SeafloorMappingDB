# Generated by Django 3.2.11 on 2022-01-27 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smdb', '0036_auto_20211203_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='track_length',
            field=models.FloatField(blank=True, null=True),
        ),
    ]