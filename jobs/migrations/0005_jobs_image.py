# Generated by Django 3.2 on 2021-04-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20210414_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='image',
            field=models.ImageField(default='', upload_to='job/'),
            preserve_default=False,
        ),
    ]
