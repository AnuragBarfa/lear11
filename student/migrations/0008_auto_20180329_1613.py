# Generated by Django 2.0.3 on 2018-03-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20180329_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='semester',
            field=models.CharField(choices=[('1st semester', '1st semester'), ('2nd semester', '2nd semester'), ('3rd semester', '3rd semester'), ('4th semester', '4th semester'), ('5th semester', '5th semester'), ('6th semester', '6th semester'), ('7th semester', '7th semester'), ('8th semester', '8th semester'), ('For All', 'For All')], default=' ', max_length=50),
        ),
    ]
