from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'body']

admin.site.register(Note, NoteAdmin)
