# Generated by Django 3.2 on 2021-04-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='date_join',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
