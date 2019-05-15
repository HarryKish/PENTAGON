from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


# Create your models here.
class Criminal(models.Model):
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mugshot = models.FileField()
    mugshot_no = models.IntegerField()
    fingerprint = models.FileField()
    sentence_date = models.DateTimeField(default=timezone.now())
    felony_description = models.TextField()
    sentencing_description = models.TextField()
    prisonname = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('judiciary:index')


    def __str__(self):
        return self.firstname

