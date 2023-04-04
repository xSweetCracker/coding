from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_taskmaster',
        'is_master'
    )


@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brigade_id',
        'workers'
    )


@admin.register(ObjWorks)
class ObjWorksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'works_brigade'
    )
