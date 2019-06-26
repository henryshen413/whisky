# Generated by Django 2.1.7 on 2019-06-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0010_auto_20190615_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whiskyinfo',
            old_name='bottling',
            new_name='bottler',
        ),
        migrations.AddField(
            model_name='whiskyinfo',
            name='artificial_coloring',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='no', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whiskyinfo',
            name='bottle_num',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='whiskyinfo',
            name='brand_series',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='whiskyinfo',
            name='cask_num',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='whiskyinfo',
            name='chill_filtration',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whiskyinfo',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]