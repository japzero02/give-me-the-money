from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def display_student(request):
    """Show student database in html"""
    items = Student.objects.all()
    context = {
        'items': items,
        'header': 'Student',
    }
    return render(request, 'index.html', context)


def add_student(request):
    """add student"""
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
        return render(request, 'add_new.html', {'form': form})
