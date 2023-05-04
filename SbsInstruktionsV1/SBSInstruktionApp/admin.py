from django.contrib import admin

from .models import Anleitung, Anleitungsschritt, Komponente

# Register your models here.

admin.site.register(Anleitung)
admin.site.register(Anleitungsschritt)
admin.site.register(Komponente)