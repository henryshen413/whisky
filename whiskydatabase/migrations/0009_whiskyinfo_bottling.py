# Generated by Django 2.1.7 on 2019-06-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0008_auto_20190614_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiskyinfo',
            name='bottling',
            field=models.CharField(choices=[('OB', 'OB'), ('IB', 'IB')], default='OB', max_length=2),
            preserve_default=False,
        ),
    ]