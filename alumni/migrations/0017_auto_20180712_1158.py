# Generated by Django 2.0.3 on 2018-07-12 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0016_auto_20180706_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_image',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Person'),
        ),
    ]