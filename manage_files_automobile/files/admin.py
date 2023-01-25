from django.contrib import admin
from .models import Automobile, Part, File

# Register your models here.


@admin.register(Automobile)
class AutomobileAdmin(admin.ModelAdmin):
    pass


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    pass


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
