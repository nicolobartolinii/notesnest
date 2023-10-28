from django.shortcuts import render
from .models import Notes


def home(request):
    notes = Notes.objects.all()
    return render(request, 'home.html', {'notes': notes})
