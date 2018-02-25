# Generated by Django 2.0.1 on 2018-02-10 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180207_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_until', models.DateTimeField(verbose_name='Дата окончания действия ссылки активации')),
                ('url', models.URLField(verbose_name='Ссылка')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='activation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Activation', verbose_name='Активация'),
        ),
    ]