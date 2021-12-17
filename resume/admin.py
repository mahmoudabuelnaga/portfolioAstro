from django.contrib import admin
from . import models

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ImageInline(admin.TabularInline):
    model = models.portfolioImg
    #row_id_field = ['img']

@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInline]

@admin.register(models.Home)
class HomeAdmin(SummernoteModelAdmin):
    summernote_fields = ('summary','about',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    
admin.site.register(models.portfolioImg)
#admin.site.register(models.Home)
