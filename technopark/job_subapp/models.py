from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    website=models.URLField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    title=models.CharField(max_length=100)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='jobs')
    description=models.TextField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    job_type=[
        ('fulltime','FULL TIME'),
        ('parttime','PART TIME'),
        ('internship','INTERNSHIP'),
        ('contract','CONTRACT'),
    ]
    job=models.CharField(max_length=100,choices=job_type,default='fulltime')
    status_1=[
        ('open','OPEN'),
        ('closed','CLOSED')
    ]
    status=models.CharField(max_length=100,choices=status_1,default='open')
    posted_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    