from django.contrib import admin

#importation des models
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Specialisation)
class SpecialisationAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'nom',
        'id_specialite',
        'status',
        'date_add',
        'date_upd',
        'view_image',
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

    readonly_fields = ['detail_image']

    fieldsets = [
        ('Information', {'fields' : ['nom', 'description', 'image', 'id_specialite' ]}),
        ('Standard', {'fields' : ['status', 'date_upd']}),
    ]


    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Specialisations sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Specialisations sélectionnées'

    def view_image(self, obj):
        return mark_safe('<img src="{img_url}" width="100px" height="50" />'.format(img_url=obj.image.url))

    def detail_image(self, obj):
        return mark_safe('<img src="{img_url}" width="300px" height="150" />'.format(img_url=obj.image.url))

@admin.register(models.UserSpecialite)
class UserSpecialiteAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'user',
        'specialite',
        'status',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'user',
        'specialite',
    )

    # search_fields = (
    #     'nom',
    # )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    # list_display_links = ['nom',]
    
    list_per_page = 10

    # ordering = ['nom',]

    # readonly_fields = ['detail_image']
    fieldsets = [
        ('Information', {'fields' : ['user', 'specialite' ]}),
        ('Standard', {'fields' : ['status', 'date_upd']}),
    ]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Specialit"s sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Specialités sélectionnées'

    # def viw_image(self, obj):
    #     return mark_safe('<img src="{img_url}" width="100px" height="50" />'.format(img_url=obj.image.url))

    # def detail_image(self, obj):
    #     return mark_safe('<img src="{img_url}" width="300px" height="150" />'.format(img_url=obj.image.url))

@admin.register(models.Niveau)
class NiveauAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'nom',
        'date_add',
        'status',
        'date_upd',
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

    list_display_links = ['nom']
    
    list_per_page = 10

    ordering = ['nom',]

    fieldsets = [
        ('Information', {'fields' : ['nom', 'description' ]}),
        ('Standard', {'fields' : ['status', 'date_upd']}),
    ]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Niveaux sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les niveaux sélectionnées'


@admin.register(models.Cours)
class CoursAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'niveau',
        'specialisation',
        'titre',
        'date_add',
        'date_upd',
        'status',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'specialisation',
        'niveau',

    )

    search_fields = (
        'titre',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['titre']
    
    list_per_page = 10

    ordering = ['titre',]
    fieldsets = [
        ('Information', {'fields' : ['titre', 'niveau', 'description', 'specialisation' ]}),
        ('Standard', {'fields' : ['status', 'date_upd']}),
    ]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Cours sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les cours sélectionnées'


@admin.register(models.Ressources)
class RessourceAdmin(admin.ModelAdmin):
    
    #les champs à afficher dans la table
    list_display = (
        'cours',
        'link',
        'types',
        'status',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'cours',
        'types',
    )

    search_fields = (
        'types',
    )

    list_display_links = ['types']
    
    list_per_page = 10

    ordering = ['types',]


    fieldsets = [
        ('Information', {'fields' : ['cours']}),
        ('Ressources', {'fields' : ['link', 'types']}),
        ('Standard', {'fields' : ['status', 'date_upd']}),
    ]
    

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Ressources sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Ressources sélectionnées'
    

@admin.register(models.Composition)
class CompositionAdmin(admin.ModelAdmin):
    
    #les champs à afficher dans la table
    list_display = (
        'cours',
        'date_debut',
        'date_fin',
        'status',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'cours',
        'date_debut',
        'date_fin',


    )


    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['cours']
    
    list_per_page = 10

    ordering = ['date_debut',]


    fieldsets = [
        ('Information', {'fields' : ['Cours', 'date_debut', 'date_fin']}),
        ('Standard', {'fields' : ['status', 'date_upd']}),
    ]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Compositions sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Compositions sélectionnées'

    # def view_video(self, obj):
    #     return mark_safe('<video controls width="250"><source src="{video_url}" type="video/webm"><source src="{video_url}" type="video/mp4"></video>'.format(video_url=obj.video.url))

@admin.register(models.ResultatCompos)
class ResultatComposAdmin(admin.ModelAdmin):
    
    #les champs à afficher dans la table
    list_display = (
        'user',
        'rang',
        'note',
        'status',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['user']
    
    list_per_page = 10

    ordering = ['rang',]


    fieldsets = [
        ('Information', {'fields' : ['user', 'note', 'rang']}),
        ('Standard', {'fields' : ['status', 'date_upd']}),
    ]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Resultats Compos sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Resultats Compos sélectionnées'
