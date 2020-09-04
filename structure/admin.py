from django.contrib import admin

from .models import *


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at', 'updated_at', 'is_published')
#     list_display_links = ('title', 'created_at', 'updated_at', 'is_published')
#     search_fields = ('title', 'anons', 'content')

class GalleryInline(admin.TabularInline):
    fk_name = 'keyBranches'
    model = GalleryBranches


@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
