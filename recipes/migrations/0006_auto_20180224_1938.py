# Generated by Django 2.0.2 on 2018-02-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20180224_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Картинка'),
        ),
    ]
