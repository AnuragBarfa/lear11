# Generated by Django 2.0.3 on 2018-08-22 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20180823_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email_link',
        ),
        migrations.RemoveField(
            model_name='student',
            name='fb_link',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ln_link',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile_img',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
    ]
