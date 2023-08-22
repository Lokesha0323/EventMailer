from django.db import models

class Event(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    event_date = models.DateField()
    sent_status = models.CharField(max_length=10)

class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=50)
    template_content = models.TextField()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
