from django.shortcuts import render, redirect, get_object_or_404
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


def edit_student(request, pk):
    """edit student by primarykey"""
    item = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})
