# Generated by Django 2.2.2 on 2019-06-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step_tracker', '0002_auto_20190616_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steps',
            name='activitiy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='steps',
            name='minutes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]