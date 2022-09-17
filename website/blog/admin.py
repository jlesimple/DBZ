from django.contrib import admin
from blog.models import *

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'race')

class SagaAdmin (admin.ModelAdmin):
    list_display = ('title', 'chap_start', 'chap_stop')

admin.site.register(Character, CharacterAdmin)
admin.site.register(Saga, SagaAdmin)
admin.site.register(Place)
