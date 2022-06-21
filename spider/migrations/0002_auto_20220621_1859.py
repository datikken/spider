# Generated by Django 3.2.13 on 2022-06-21 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linktocrawl',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linktocrawl',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]