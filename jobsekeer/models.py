
from django.db import models
from register.models import RegisterUser
from jobposter.models import Job_Post

class Job_Sekeer(models.Model):
    gender = {
        ("MALE","MALE"),
        ("FEMALE","FEMALE"),
        ("NOT TO SAY","NOT TO SAY")
    }
    email = models.OneToOneField(RegisterUser, verbose_name="email", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=20,choices=gender,default="Not Selected")
    higher_educations = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BookMarked_Jobs(models.Model):
    job_id = models.ForeignKey(Job_Post,verbose_name="title",on_delete=models.CASCADE)
    job_sekeer_id = models.ForeignKey(Job_Sekeer,verbose_name="name",on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.job_id
