# Generated by Django 2.2.4 on 2019-08-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0003_auto_20190818_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'student'), (1, 'teacher'), (2, 'others')], default=0),
        ),
    ]
