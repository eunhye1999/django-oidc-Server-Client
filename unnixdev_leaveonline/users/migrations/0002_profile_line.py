# Generated by Django 2.2.1 on 2019-05-29 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='line',
            field=models.CharField(default=None, null=True, max_length=100),
            preserve_default=False,
        ),
    ]