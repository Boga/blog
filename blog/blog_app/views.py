from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from taggit.models import Tag

from .models import Note


class NotesIndexView(generic.ListView):
    template_name = 'blog_app/notes_index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(pub_date__lte=timezone.now()).order_by(
            '-pub_date')[:50]


def note_details_view(request, url):
    note = get_object_or_404(Note, url=url)
    return render(request, 'blog_app/note_details.html', {'note': note})


def tag_notes(request, slug):
    ctx = {
        'tag': get_object_or_404(Tag, slug=slug),
        'notes': Note.objects.filter(tags__slug=slug),
    }
    return render(request, 'blog_app/notes_index.html', ctx)

