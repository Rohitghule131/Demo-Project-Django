# Generated by Django 4.0.5 on 2022-07-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobposter', '0002_job_post_applied_candidate_count_job_post_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='job_type',
            field=models.CharField(choices=[('tech', 'tech'), ('non-tech', 'non-tech')], default='tech', max_length=20),
        ),
    ]
