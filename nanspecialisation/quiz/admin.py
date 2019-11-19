from django.contrib import admin

# Register your models here.

# vim: set fileencoding=utf-8 :
from django.utils.safestring import mark_safe
from . import models


class SpecialisationAdmin(admin.ModelAdmin):

    list_display = (
        'statut',
        'date_add',
        'date_update',
        'nom',
        'langage',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )
    date_hierarchy = ('date_add')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialisation', 'statut', 'date_add', 'date_update', 'view_image')
    list_filter = ('statut', 'date_add', 'date_update',)
    date_hierarchy = ('date_add')


    def view_image(self,obj):
        return mark_safe('<img src="{img_url}" width="100px", heigth="100px"/>'.format(img_url=obj.image.url))


class QuestionInline(admin.TabularInline):
    model =  models.Question
    extra = 0


class QuizzAdmin(admin.ModelAdmin):

    list_display = (
        'statut',
        'date_add',
        'date_update',
        'specialisation',
        'titre',
        'niveau',
        'pourcentage',
        'nbq',
        'date_debut',
        'date_fin',
        'duree',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'date_debut',
        'date_fin',
    )
    date_hierarchy = ('date_add')


    inlines = [QuestionInline]

class ReponseInline(admin.TabularInline):
    model =  models.Reponse
    extra = 0

class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        'statut',
        'date_add',
        'date_update',
        'quizz',
        'niveau',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'quizz',
    )
    date_hierarchy = ('date_add')

    inlines = [ReponseInline]


class ReponseAdmin(admin.ModelAdmin):

    list_display = (
        'statut',
        'date_add',
        'date_update',
        'isrtue',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'isrtue',
    )
    date_hierarchy = ('date_add')



class QuizzUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'quizz',
        'user',
        'note',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'note',
    )
    date_hierarchy = ('date_add')



class ReponseUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'quizzuser',
        'istrue',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'istrue',
    )
    date_hierarchy = ('date_add')

    raw_id_fields = ('reponses',)
    def save_related(self, request, form, formsets, change):
        super(ReponseUserAdmin, self).save_related(request, form, formsets, change)
        form.instance.save()


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Specialisation, SpecialisationAdmin)
_register(models.Profile, ProfileAdmin)
_register(models.Quizz, QuizzAdmin)
_register(models.Question, QuestionAdmin)
_register(models.Reponse, ReponseAdmin)
_register(models.QuizzUser, QuizzUserAdmin)
_register(models.ReponseUser, ReponseUserAdmin)