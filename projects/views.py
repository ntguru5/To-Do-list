from django.shortcuts import render, get_list_or_404, redirect
from projects.models import Project
# Create your views here.


def list_projects(request):
    projects = Project.objects.all()
    context = {
        "list_projects": projects,
    }
    return render(request, "projects/list.html", context)
