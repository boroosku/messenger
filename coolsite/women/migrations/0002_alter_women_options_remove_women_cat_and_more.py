# Generated by Django 4.0.5 on 2022-06-30 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create', 'title'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Пост'},
        ),
        migrations.RemoveField(
            model_name='women',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='women',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='women',
            name='slug',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
