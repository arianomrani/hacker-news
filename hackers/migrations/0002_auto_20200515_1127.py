# Generated by Django 3.0.6 on 2020-05-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'آدرس', 'verbose_name_plural': 'آدرس ها'},
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
    ]