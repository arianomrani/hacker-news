# Generated by Django 3.0.6 on 2020-05-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackers', '0002_auto_20200515_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='vote',
            field=models.IntegerField(default=0, verbose_name='رای'),
        ),
    ]
