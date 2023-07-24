from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
# Create your views here.


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": projects,
    }
    return render(request, "projects/list.html", context)
