from django.contrib import admin

from .models import Note, AttachedFile


class AttachedFileInlineAdmin(admin.TabularInline):
    model = AttachedFile


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'body']
    inlines = [AttachedFileInlineAdmin]


admin.site.register(Note, NoteAdmin)
# admin.site.register(Image)
