# Generated by Django 4.0.5 on 2022-07-01 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsekeer', '0004_alter_job_sekeer_gender_bookmarked_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarked_jobs',
            name='job_sekeer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsekeer.job_sekeer', verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='job_sekeer',
            name='gender',
            field=models.CharField(choices=[('NOT TO SAY', 'NOT TO SAY'), ('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='Not Selected', max_length=20),
        ),
    ]
