from django.contrib import admin

from .models import (Clientapp, Compteclient, Domaine, Prestataire, Profilprestataire, Serviceapp,
Servicedemandee)
# Register your models here.

#1- afffichage des tables sans les relations
@admin.register(Clientapp)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom_client', 'prenom_client','telephone_client']

@admin.register(Compteclient)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Domaine)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['label_domaine']

@admin.register(Prestataire)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom_prestataire', 'prenom_prestataire','telephone_prestaire']

@admin.register(Profilprestataire)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Serviceapp)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['label_service']

@admin.register(Servicedemandee)
class ClientAdmin(admin.ModelAdmin):
    pass






