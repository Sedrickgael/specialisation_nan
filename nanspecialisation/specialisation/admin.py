# from django.contrib import admin

# #importation des models
# from . import models
# from django.utils.safestring import mark_safe


# @admin.register(models.Specialisation)
# class SpecialisationAdmin(admin.ModelAdmin):

#     #les champs à afficher dans la table
#     list_display = (
#         'nom',
#         'id_specialite',
#         'status',
#         'date_add',
#         'viw_image,'
#         )
#     list_filter = (
#         'status',
#         'date_add',
#         'date_upd',
#     )

#     search_fields = (
#         'nom',
#         'id_specialite',
#     )

#     date_hierarchy = 'date_add'

#     actions = ('active', 'desactive')

#     list_display_links = ['nom',]
    
#     list_per_page = 10

#     ordering = ['nom',]

#     readonly_fields = ['detail_image']


#     def active(self, request, queryset):
#         queryset.update(status=True)
#         self.message_user(request, "La sélection a été activée avec succès")
#     active.short_description = 'Activez les Specialisations sélectionnées'

#     def desactive(self, request, queryset):
#         queryset.update(status=False)
#         self.message_user(request, "La sélection a été désactivée avec succès")
#     desactive.short_description = 'Désactivez les Specialisations sélectionnées'

#     def viw_image(self, obj):
#         return mark_safe('<img src="{img_url}" width="100px" height="50" />'.format(img_url=obj.image.url))

#     def detail_image(self, obj):
#         return mark_safe('<img src="{img_url}" width="300px" height="150" />'.format(img_url=obj.image.url))


# @admin.register(models.Ressources)
# class RessourceAdmin(admin.ModelAdmin):
    
#     #les champs à afficher dans la table
#     list_display = (
#         'cours',
#         'status',
#         'date_add',
#         'date_upd',
            
#         )
#     list_filter = (
#         'status',
#         'date_add',
#         'date_upd',
#         'cours',
#     )

#     search_fields = (
#         'titre',
#     )

#     date_hierarchy = 'date_add'

#     actions = ('active', 'desactive')

#     # list_display_links = ['titre']
    
#     list_per_page = 3

#     # ordering = ['titre',]


#     fieldsets = [
#         ('Information', {'fields' : ['Cours']}),
#         ('Ressources', {'fields' : ['pdf', 'video']}),
#         ('Standar', {'fields' : ['status', 'date_upd']}),
#     ]

#     def active(self, request, queryset):
#         queryset.update(status=True)
#         self.message_user(request, "La sélection a été activée avec succès")
#     active.short_description = 'Activez les Ressources sélectionnées'

#     def desactive(self, request, queryset):
#         queryset.update(status=False)
#         self.message_user(request, "La sélection a été désactivée avec succès")
#     desactive.short_description = 'Désactivez les Ressources sélectionnées'

#     # def view_video(self, obj):
#     #     return mark_safe('<video controls width="250"><source src="{video_url}" type="video/webm"><source src="{video_url}" type="video/mp4"></video>'.format(video_url=obj.video.url))

    
