# Generated by Django 4.0.6 on 2022-07-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forwork', '0004_staf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='Kategor',
            field=models.CharField(choices=[('специалист', 'специалист'), ('служащий', 'служащий'), ('рабочий', 'рабочий')], max_length=20, verbose_name='Kategory'),
        ),
        migrations.AlterField(
            model_name='role',
            name='Name',
            field=models.CharField(default='', max_length=40, verbose_name='Name'),
        ),
    ]
