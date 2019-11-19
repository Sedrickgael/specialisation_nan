from django.db import models
from specialisation.models import * 

# Create your models here.

class Exercice(models.Model):
    """Model definition for Exercice."""

    titre = models.CharField(max_length=255)
    description = HTMLField('description')
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,related_name='niveauexercice')
    code_depart = models.TextField()
    specialite = models.ForeignKey(Specialisation, on_delete=models.CASCADE,related_name='specialiteexercice')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Exercice."""

        verbose_name = 'Exercice'
        verbose_name_plural = 'Exercices'

    def __str__(self):
        """Unicode representation of Exercice."""
        return '{}'.format(self.titre ) # TODO

class TestValidation(models.Model):
    """Model definition for TestValidation."""

    code_test = models.TextField()
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE,related_name='exercicetest')
    resultat = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for TestValidation."""

        verbose_name = 'TestValidation'
        verbose_name_plural = 'TestValidations'

    def __str__(self):
        """Unicode representation of TestValidation."""
        return '{}'.format(self.resultat ) # TODO

class ResultatExercice(models.Model):
    """Model definition for ResultatExercice."""

    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE,related_name='exerciceresultat')
    nb_tentative = models.PositiveIntegerField()
    code = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='userresultat')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    

    class Meta:
        """Meta definition for ResultatExercice."""

        verbose_name = 'ResultatExercice'
        verbose_name_plural = 'ResultatExercices'

    def __str__(self):
        """Unicode representation of ResultatExercice."""
        return '{}'.format(self.user ) # TODO

class ResultatCompo(models.Model):
    """Model definition for ResultatCompo."""

    resultat_exercice = models.ForeignKey(ResultatExercice, on_delete=models.CASCADE,related_name='resultexoresultcompo')
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,related_name='niveauresultatcompo')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='resultatcompouser')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for ResultatCompo."""

        verbose_name = 'ResultatCompo'
        verbose_name_plural = 'ResultatCompos'

    def __str__(self):
        """Unicode representation of ResultatCompo."""
        return '{}'.format(self.user.username ) # TODO