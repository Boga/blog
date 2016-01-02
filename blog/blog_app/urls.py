from django.conf.urls import url

from . import views

app_name = 'blog_app'
urlpatterns = [
    # ex: /
    url(r'^$', views.NotesIndexView.as_view(), name='notes_index'),
    # ex: /note/3
    url(r'^note/(?P<url>[\w-]+)', views.note_detail_view, name='note_details'),
]