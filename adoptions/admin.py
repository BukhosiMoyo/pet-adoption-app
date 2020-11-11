from django.contrib import admin
from .models import *


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']



@admin.register(Submitter)
class SubmitAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ('name', 'email', 'phone')


