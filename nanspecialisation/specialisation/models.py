from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
# Create your models here.

class Specialisation(models.Model):
    nom = models.CharField( max_length=250)
    image = models.FileField(upload_to="specialite/image")
    description = HTMLField('description')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    id_specialite = models.PositiveIntegerField(null=True, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Specialisation."""

        verbose_name = 'Specialisation'
        verbose_name_plural = 'Specialisations'

    def __str__(self):
        """Unicode representation of Specialisation."""
        return self.nom


class UserSpecialite(models.Model):
    """Model definition for UserSpecialite."""
    user = models.ForeignKey(User,related_name='user_specialite',on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialisation, on_delete=models.CASCADE,related_name='specialiteuser')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for UserSpecialite."""

        verbose_name = 'UserSpecialite'
        verbose_name_plural = 'UserSpecialites'

    def __str__(self):
        """Unicode representation of UserSpecialite."""
        return '{}:{}'.format(self.user.username,self.specialite.nom ) # TODO

    def __str__(self):
        """Unicode representation of UserSpecialite."""
        return '{}:{}'.format(self.user.username,self.specialite.nom ) # TODO

class Niveau(models.Model):
    """Model definition for Niveau."""

    nom = models.CharField(max_length=255)
    description = HTMLField('description')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Niveau."""

        verbose_name = 'Niveau'
        verbose_name_plural = 'Niveaus'

    def __str__(self):
        """Unicode representation of Niveau."""
        return '{}'.format(self.nom ) # TODO

class Cours(models.Model):
    """Model definition for Cours."""

    titre = models.CharField(max_length=250)
    niveau = models.ForeignKey(Niveau,on_delete=models.CASCADE,related_name='niveaucours')
    description = models.TextField()
    specialisation = models.ForeignKey(Specialisation, on_delete=models.CASCADE, related_name="specialisation")
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        """Meta definition for Cours."""

        verbose_name = 'Cours'
        verbose_name_plural = 'Courss'
    
    def __str__(self):
        """Unicode representation of Niveau."""
        return self.titre

class Ressources(models.Model):
    """Model definition for Ressources."""

    cours = models.ForeignKey(Cours, on_delete=models.CASCADE,related_name='coursressources')
    link = models.URLField()
    types = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    
    class Meta:
        """Meta definition for Cours."""

        verbose_name = 'Ressources'
        verbose_name_plural = 'Ressources'

    def __str__(self):
        """Unicode representation of Ressources."""
        return '{}'.format(self.cours) # TODO

class Composition(models.Model):
    """Model definition for Composition."""

    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name="cours_composition")
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Composition."""

        verbose_name = 'Composition'
        verbose_name_plural = 'Compositions'

    def __str__(self):
        """Unicode representation of Composition."""
        return self.cours.titre

class ResultatCompos(models.Model):
    """Model definition for ResultatCompos."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_resultat")
    rang = models.PositiveIntegerField()
    note = models.FloatField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        """Meta definition for Composition."""

        verbose_name = 'ResultatCompos'
        verbose_name_plural = 'ResultatComposs'

    def __str__(self):
        """Unicode representation of ResultatCompos."""
        return "{}".format(self.user.username)

