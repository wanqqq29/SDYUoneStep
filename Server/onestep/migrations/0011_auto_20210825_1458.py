# Generated by Django 3.1.3 on 2021-08-25 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onestep', '0010_auto_20210806_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsline',
            options={'get_latest_by': 'subtitle'},
        ),
    ]
