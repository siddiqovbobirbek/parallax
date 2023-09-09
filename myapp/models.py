from django.db import models
from django.utils.translation import gettext_lazy as _

from django.utils.html import format_html
# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


