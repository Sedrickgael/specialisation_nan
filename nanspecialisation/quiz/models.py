from django.db import models

# Create your models here.

# Projet_quizz
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from tinymce import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator
import pytz


class Timemodels(models.Model):
    statut = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Specialisation(Timemodels):
    """Model definition for Specialisation."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    langage = models.CharField(max_length=50)
    
    @property
    def classement(self):
        """Fonction pour faire le classement par spécialisation"""
        return self.users.all().order_by('-moyenne_generale')

    class Meta:
        """Meta definition for Specialisation."""

        verbose_name = 'Specialisation'
        verbose_name_plural = 'Specialisations'

    def __str__(self):
        """Unicode representation of Specialisation."""
        return self.nom


class Profile(Timemodels):
    """Model definition for UserProfile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="profile", default="omar-sy-by-rachel.jpg")
    specialisation = models.ForeignKey('Specialisation', related_name='users', on_delete=models.CASCADE, blank=True, null=True)
    moyenne_generale = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def save(self, *args, **kwargs):
        self.moyenne_generale = self.get_moyenne_general()
        super(Profile, self).save(*args, **kwargs)

    def get_moyenne_general(self):
        """ Fonction qui recupère la moyenne de l'utilisateur """
        if self.specialisation:
            notes = sum([i.note for i in self.user.quizzs.all()])
            nb = self.specialisation.quizzs.filter(statut = True).count()
            return notes/nb
        else:
            return 0

    @property
    def get_specialisation_rang(self):
        """Fonction pour récupérer le classement de l'utilisateur par spécialisation"""
        return self.specialisation.all().order_by('-moyenne_generale')

    @property
    def get_general_rang(self):
        """Fonction pour récupérer le classement général de l'utilisateur"""
        pass
    
    @property
    def get_specialisation_sexe_rang(self):
        """Fonction pour récupérer le classement de l'utilisateur par spécialisation par sexe"""
        pass
    
    @property
    def get_general_sexe_rang(self):
        """Fonction pour récupérer le classement de l'utilisateur par spécialisation"""
        pass


    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        """Unicode representation of UserProfile."""
        return self.user.username
    
    @classmethod
    def classement_general(cls):
        return cls.objet.all().order_by('-moyenne_generale')
    
    @property
    def get_general_rang(self):
        """Fonction pour récupérer le classement général de l'utilisateur"""
        pass
    
    @property
    def get_specialisation_sexe_rang(self):
        """Fonction pour récupérer le classement de l'utilisateur par spécialisation par sexe"""
        pass
    
    @property
    def get_general_sexe_rang(self):
        """Fonction pour récupérer le classement de l'utilisateur par spécialisation"""
        pass


    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        """Unicode representation of UserProfile."""
        return self.user.username
    
    @classmethod
    def classement_general(cls):
        return cls.objet.all().order_by('-moyenne_generale')


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()

class Quizz(Timemodels):
    """Model definition for Quizz."""

    # TODO: Define fields here
    specialisation = models.ForeignKey('Specialisation', related_name='quizzs', on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    niveau = models.PositiveIntegerField()
    pourcentage = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="pourcentage pour valider")
    nbq = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], verbose_name="Nombre de questions par quizz", null=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    duree = models.TimeField()
    
    

    @property
    def is_available(self):
        now = datetime.now()
        now = pytz.utc.localize(now)
        return self.date_debut < now <self.date_fin

    class Meta:
        """Meta definition for Quizz."""

        verbose_name = 'Quizz'
        verbose_name_plural = 'Quizzs'

    def __str__(self):
        """Unicode representation of Quizz."""
        return "{}: {}".format(self.specialisation, self.titre)

class Question(Timemodels):
    """Model definition for Question."""

    # TODO: Define fields here
    quizz = models.ForeignKey('Quizz', related_name='questions', on_delete=models.CASCADE)
    niveau = models.PositiveIntegerField()
    contenu =  HTMLField('question_contenu')

    @property
    def liste_true(self):
        aux = [i.id for i in self.reponses.filter(isrtue=True)]
        aux.sort()
        return aux

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.contenu

class Reponse(Timemodels):
    """Model definition for Reponse."""

    # TODO: Define fields here
    question = models.ForeignKey('Question', related_name='reponses', on_delete=models.CASCADE)
    contenu =  HTMLField('reponse_contenu')
    isrtue = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Reponse."""

        verbose_name = 'Reponse'
        verbose_name_plural = 'Reponses'

    def __str__(self):
        """Unicode representation of Reponse."""
        return self.contenu

class QuizzUser(Timemodels):
    """Model definition for QuizzUser."""

    # TODO: Define fields here
    quizz = models.ForeignKey('Quizz', related_name='quizzuser', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzs")
    note = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    class Meta:
        """Meta definition for QuizzUser."""

        verbose_name = 'QuizzUser'
        verbose_name_plural = 'QuizzUsers'
        
    def createquizz(self):
        """Fonction pour générer les questions d'un quizz"""
        pass

    def save(self, *args, **kwargs):
        nb = self.questions.all().count()
        if nb == 0:
            super(QuizzUser, self).save(*args, **kwargs)
            for q in self.quizz.questions.all():
                r = ReponseUser(
                    question = q,
                    quizzuser = self
                )
                r.save()
                nb += 1
        n = 0
        for q in self.questions.all():
            if q.istrue:
                n+=1
        self.note = round(n/nb, 4)*100
        super(QuizzUser, self).save(*args, **kwargs)
        self.user.save()

    def __str__(self):
        """Unicode representation of QuizzUser."""
        return str(self.note)


class ReponseUser(Timemodels):
    """Model definition for ReponseUser."""

    # TODO: Define fields here
    question = models.ForeignKey('Question', related_name='reponseuser', on_delete=models.CASCADE)
    quizzuser = models.ForeignKey('QuizzUser', related_name='questions', on_delete=models.CASCADE)
    reponses = models.ManyToManyField('Reponse')
    istrue = models.BooleanField(default=False)

    @property
    def liste_true(self):
        aux = [i.id for i in self.reponses.all()]
        aux.sort()
        return aux

    class Meta:
        """Meta definition for ReponseUser."""

        verbose_name = 'ReponseUser'
        verbose_name_plural = 'ReponseUsers'
    
    def save(self, *args, **kwargs):
        super(ReponseUser, self).save(*args, **kwargs)
        self.istrue = self.liste_true == self.question.liste_true
        super(ReponseUser, self).save(*args, **kwargs)
        self.quizzuser.save()

    def __str__(self):
        """Unicode representation of ReponseUser."""
        return str(self.istrue)