from django.db import models

# Create your models here.
class Website(models.Model):
    logo = models.FileField(upload_to='attachments/',blank=False, null=False)
    tagline = models.CharField(max_length=100)