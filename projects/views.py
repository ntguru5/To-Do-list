from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from .forms import CreateProjectForm

# Create your views here.


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project_detail = Project.objects.get(id=id)
    context = {
        "project_detail": project_detail,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")

    else:
        form = CreateProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)
