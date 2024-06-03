from django.shortcuts import render
from .models import Animal

# Create your views here.


def animals_list_view(request):

    animals = Animal.objects.all()
    return render(request, "animals/list.html", {"animals": animals})
