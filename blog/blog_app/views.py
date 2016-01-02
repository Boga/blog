from django.utils import timezone

from .models import Note
from django.views import generic


class NotesIndexView(generic.ListView):
    template_name = 'blog_app/notes_index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Note.objects.filter(pub_date__lte=timezone.now()).order_by(
            '-pub_date')[:50]


class NoteDetailView(generic.DetailView):
    model = Note
    template_name = 'blog_app/note_details.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Note.objects.filter(pub_date__lte=timezone.now())
