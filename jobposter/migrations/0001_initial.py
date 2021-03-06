# Generated by Django 4.0.5 on 2022-07-01 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=50)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('foreignkey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobposter.job_poster', verbose_name='email')),
            ],
        ),
    ]
