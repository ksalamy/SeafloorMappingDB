# Generated by Django 3.2.6 on 2021-09-11 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smdb', '0023_rename_mission_name_mission_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='name',
            field=models.CharField(max_length=512, null=True),
        ),
    ]