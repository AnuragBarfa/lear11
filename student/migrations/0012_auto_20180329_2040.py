# Generated by Django 2.0.3 on 2018-03-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20180329_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='semester',
            field=models.CharField(choices=[('', '-------'), ('1st_semester', '1st_semester'), ('2nd_semester', '2nd_semester'), ('3rd_semester', '3rd_semester'), ('4th_semester', '4th_semester'), ('5th_semester', '5th_semester'), ('6th_semester', '6th_semester'), ('7th_semester', '7th_semester'), ('8th_semester', '8th_semester'), ('For_All', 'For_All')], default=' ', max_length=50),
        ),
    ]