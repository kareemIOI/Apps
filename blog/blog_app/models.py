from django.db import models

# Create your models here.

class Forms(models.Model):
    first_name = models.CharField(max_length = 255)
    email = models.EmailField(_(""), max_length=254)
    Phone = models.PhoneNumberField(_(""))
    message = models.TextField()