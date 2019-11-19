from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Specialisation(models.Model):
    nom = models.CharField( max_length=250)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Specialisation."""

        verbose_name = 'Specialisation'
        verbose_name_plural = 'Specialisations'

    def __str__(self):
        """Unicode representation of Specialisation."""
        return self.nom

class Cours(models.Model):
    """Model definition for Cours."""

    titre = models.CharField(max_length=250)
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
        """Unicode representation of Cours."""
        return self.titre

class Ressource(models.Model):
    """Model definition for Ressource."""

    pdf = models.FileField(upload_to="cours/pdf", null=True)
    video = models.FileField(upload_to="cours/videos", null=True)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name="ressources_cours")
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Ressource."""

        verbose_name = 'Ressource'
        verbose_name_plural = 'Ressources'

    def __str__(self):
        """Unicode representation of Ressource."""
        return self.cours.titre

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
        """Meta definition for ResultatCompos."""

        verbose_name = 'ResultatCompos'
        verbose_name_plural = 'ResultatComposs'

    def __str__(self):
        """Unicode representation of ResultatCompos."""
        return "{}:{}".format(self.user.username, self.rang)

