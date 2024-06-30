from django.urls import path
from django.views.generic.base import TemplateView


from .views import about_page, resume_page, ProjectListView, contact_page

urlpatterns = [
    path('', about_page, name='about'),
    path('resume/', resume_page, name='resume'),
    path('project/', ProjectListView.as_view(), name='project'),
    path('contact/', contact_page, name='contact'),
]