from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def display_student(request):
    """Show student database in html"""
    items = Student.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)
