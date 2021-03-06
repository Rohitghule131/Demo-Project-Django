# Generated by Django 4.0.5 on 2022-07-01 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobsekeer', '0006_alter_job_sekeer_gender'),
        ('jobposter', '0004_alter_job_post_job_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applied_Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobposter.job_post', verbose_name='job')),
                ('job_sekeer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsekeer.job_sekeer', verbose_name='talent')),
            ],
        ),
    ]
