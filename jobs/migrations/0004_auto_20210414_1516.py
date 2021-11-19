# Generated by Django 3.2 on 2021-04-14 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.category'),
        ),
    ]