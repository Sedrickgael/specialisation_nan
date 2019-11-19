from django.contrib import admin

#importation des models
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Specialisation)
class SpecialisationAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'nom',
        'status',
        'date_add',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = (
        'nom',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['nom',]
    
    list_per_page = 10

    ordering = ['nom',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Specialisations sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Specialisations sélectionnées'

    
@admin.register(models.Cours)
class CoursAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'specialisation',
        'titre',
        'date_add',
        'status',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'specialisation',
    )

    search_fields = (
        'titre',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['titre',]
    
    list_per_page = 10

    ordering = ['titre',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Cours sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Cours sélectionnées'

@admin.register(models.Ressource)
class RessourceAdmin(admin.ModelAdmin):
    
    #les champs à afficher dans la table
    list_display = (
        'cours',
        'status',
        'date_add',
        'date_upd',
        'view_video',
            
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'cours',
    )

    search_fields = (
        'categorie',
        'tague',
        'titre',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['titre', 'view_image']
    
    list_per_page = 3

    ordering = ['titre',]

    readonly_fields = ['detail_image']

    fieldsets = [
        ('Information', {'fields' : ['Cours']}),
        ('Ressources', {'fields' : ['pdf', 'video']}),
        ('Standar', {'fields' : ['status', 'date_upd']}),
    ]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Ressources sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Ressources sélectionnées'

    def view_video(self, obj):
        return mark_safe('<video controls width="250"><source src="{video_url}" type="video/webm"><source src="{video_url}" type="video/mp4"></video>'.format(video_url=obj.video.url))

    
