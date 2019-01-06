from django.contrib import admin
import test1.models as models
# Register your models here.

admin.site.register(models.Musician)
admin.site.register(models.Album)