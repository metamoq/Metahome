# Generated by Django 2.0.1 on 2018-01-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default='Title', max_length=100),
        ),
    ]