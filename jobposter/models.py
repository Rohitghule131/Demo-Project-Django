from django.db import models
from register.models import RegisterUser
from datetime import date
class Job_Poster(models.Model):
    email = models.OneToOneField(RegisterUser, verbose_name="email", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Job_Post(models.Model):
    job_types = {
        ("tech","tech"),
        ("non-tech","non-tech")
    }
    foreignkey_id = models.ForeignKey(Job_Poster, verbose_name="email", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(default="text")
    job_type = models.CharField(max_length=20,choices=job_types,default="tech")
    created_at = models.DateField(null=False,default=date.today())
    job_opening = models.IntegerField(default=0)
    job_role = models.CharField(max_length=20,default="null")
    salary_package = models.CharField(max_length=20,default="null")
    applied_candidate_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
