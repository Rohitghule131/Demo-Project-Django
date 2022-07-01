from django.db import models
from jobposter.models import Job_Post
from jobsekeer.models import Job_Sekeer

class Applied_Job(models.Model):
    job_post = models.ForeignKey(Job_Post, verbose_name="job", on_delete=models.CASCADE)
    job_sekeer = models.ForeignKey(Job_Sekeer, verbose_name="talent", on_delete=models.CASCADE)

