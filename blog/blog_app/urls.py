from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'blog_app'
urlpatterns = [
    # ex: /
    url(r'^$', views.NotesIndexView.as_view(), name='notes_index'),
    # ex: /note/3
    url(r'^note/(?P<url>[\w-]+)', views.note_detail_view, name='note_details'),
    # /about
    url(r'^about/', TemplateView.as_view(template_name="blog_app/about.html")),
    url(r'^resume/',
        TemplateView.as_view(template_name="blog_app/resume.html")),
    url(r'^projects/', TemplateView.as_view(
            template_name="blog_app/projects.html")),
]
