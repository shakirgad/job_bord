# Generated by Django 3.2 on 2021-04-18 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_jobs_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('website', models.URLField()),
                ('load_cv', models.FileField(upload_to=None)),
                ('note', models.TextField(max_length=1000)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobs')),
            ],
        ),
    ]