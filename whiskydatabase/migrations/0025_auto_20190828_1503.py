# Generated by Django 2.2.4 on 2019-08-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0024_bar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bar',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='distillery',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='distillery',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]