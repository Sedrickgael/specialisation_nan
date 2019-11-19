from django.db import models
from specialisation.models import * 

# Create your models here.

class UserSpecialite(models.Model):
    """Model definition for UserSpecialite."""
    user = models.ForeignKey(User,related_name='user_specialite',on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialisation, on_delete=models.CASCADE,related_name='specialiteuser')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Meta:
    """Meta definition for UserSpecialite."""

    verbose_name = 'UserSpecialite'
    verbose_name_plural = 'UserSpecialites'

def __str__(self):
    """Unicode representation of UserSpecialite."""
    return '{}:{}'.format(self.user.username,self.specialite.nom ) # TODO