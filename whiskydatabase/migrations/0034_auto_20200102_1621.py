# Generated by Django 3.0.1 on 2020-01-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0033_auto_20190920_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whiskyinfo',
            name='artificial_coloring',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='whiskyinfo',
            name='chill_filtration',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
    ]