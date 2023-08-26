from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.

projecstList = [
    {"id":1,"title":"Gan","description":"Other specified diabetes mellitus with proliferative diabetic retinopathy with traction retinal detachment involving the macula"},
    {"id":2,"title":"Giselle","description":"Displaced fracture of lateral end of right clavicle, subsequent encounter for fracture with malunion"},
    {"id":3,"title":"Lowe","description":"Acute dacryocystitis of left lacrimal passage"},
    {"id":4,"title":"Wells","description":"Phlebitis and thrombophlebitis of right femoral vein"},
    {"id":5,"title":"Ginger","description":"Nondisplaced fracture of triquetrum [cuneiform] bone, left wrist, initial encounter for open fracture"},
    {"id":6,"title":"Jennifer","description":"Contact with steam and hot vapors, undetermined intent"},
    {"id":7,"title":"Teodora","description":"Corrosion of first degree of lip(s)"},
    {"id":8,"title":"Everard","description":"Zellweger syndrome"},
    {"id":9,"title":"Roseann","description":"Muscle wasting and atrophy, not elsewhere classified, right shoulder"},
    {"id":10,"title":"Margarethe","description":"Ganglion, right ankle and foot"},
    {"id":11,"title":"Morse","description":"Superficial foreign body, unspecified hip, initial encounter"},
    {"id":12,"title":"Rainer","description":"X-linked adrenoleukodystrophy, unspecified type"}
]

def projects(request):
    projecstListt = Project.objects.all()
    return render(request,'projects/projects.html',{"projecstList":projecstListt})

def project(request,pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    return render(request,'projects/single-project.html',{"project":projectobj, 'tags':tags})

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form':form}
    return render(request, "projects/project_form.html", context)

def updateProject(request, pk):
    project = project.objects.get(id=pk)
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project )
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form':form}
    return render(request, "projects/project_form.html", context)