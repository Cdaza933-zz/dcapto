from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class BlockUser(AbstractUser):
    phone_number = models.CharField(max_length=255, null=False, blank=False)
    document_number = models.CharField(max_length=255, null=False, blank=False)
    apto_number = models.CharField(max_length=255, null=False, blank=False)


class BlockEmailSender(models.Model):
    subject = models.CharField(max_length=255, null=False, blank=False)
    email_html = models.TextField(max_length=255, null=False, blank=False)
    email_name = models.CharField(max_length=255, null=False, blank=False)
    email_description = models.CharField(max_length=255, null=False, blank=False)
