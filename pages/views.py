from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_list_or_404

from .models import Project_Rezome
def about_page(request):
    return render(request, "about.html")


def resume_page(request):
    coding_skills = { 'django': 64, 'python': 46, 'git': 40, 'html': 25, 'docker': 23, 'css': 10,}
    return render(request, "resume.html", {'coding_skills': coding_skills})


# def project_page(request):
#     projects = Project_Rezome
#     return render(request, "project.html", {"projects": projects})


class ProjectListView(generic.ListView):
    model = Project_Rezome
    template_name = "project.html"
    context_object_name = "projects"




def contact_page(request):
    return render(request, "contact.html")
