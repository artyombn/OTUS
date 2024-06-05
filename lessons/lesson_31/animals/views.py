from django.shortcuts import render
from .models import Animal

# Create your views here.


def animals_list_view(request):

    # animals = Animal.objects.all()

    # Чтобы подгрузить сразу связанные данные во избежание дубликатов запросов в БД
    animals = Animal.objects.select_related("category").prefetch_related("food").all()
    return render(request, "animals/list.html", {"animals": animals})
