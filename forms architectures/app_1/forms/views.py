from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


# Create your views here.
def index(request):
    form = ProjectForm()
    
    context = {'form': form}
    
    return render(request, 'index.html', context)