# Generated by Django 2.0.3 on 2018-08-22 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('alumni', '0018_auto_20180712_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='user',
        ),
        migrations.AddField(
            model_name='alumni',
            name='person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Person'),
        ),
    ]