from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import csv, io
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def display_student(request):
    """Show student database in html"""
    items = Student.objects.all().order_by('student_id')
    context = {
        'items': items,
        'header': 'Student',
    }
    return render(request, 'index.html', context)


def add_student(request):
    """this function can add student in add_new.html"""
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/display_student')
    else:
        form = StudentForm()
        return render(request, 'add_new.html', {'form': form})


def edit_student(request, pk):
    """this function can edit student form in edit_item.html"""
    item = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/display_student')
    else:
        form = StudentForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})


def delete_student(request, pk):
    """this function can delete student information"""
    Student.objects.filter(id=pk).delete()
    items = Student.objects.all()
    context = {
        'items': items
    }
    return redirect('/display_student')


def upload_csv(request):
    """this function can add student by csv file"""
    template = "upload_csv.html"
    data = Student.objects.all()
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This not csv file please try again!')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Student.objects.update_or_create(
            student_id=column[0],
            first_name=column[1],
            last_name=column[2]
        )
    context = {}
    return redirect('/display_student')
