# Generated by Django 2.1.7 on 2019-06-14 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0007_distillery_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('icon', models.CharField(blank=True, default='fa fa-search', max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
                ('lvl', models.IntegerField(blank=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='whiskydatabase.Menu')),
            ],
        ),
        migrations.AlterField(
            model_name='whiskyinfo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='whisky/uploads/%Y/%m/%d/'),
        ),
    ]