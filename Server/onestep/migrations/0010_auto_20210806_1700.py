# Generated by Django 3.1.3 on 2021-08-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onestep', '0009_newsline_href'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsline',
            name='id',
        ),
        migrations.AlterField(
            model_name='newsline',
            name='title',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
