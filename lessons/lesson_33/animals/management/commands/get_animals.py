import random
from django.core.management.base import BaseCommand
from animals.models import Category, Animal, Food


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Get animals ...")

        print("Получить все категории")
        print(Category.objects.all())

        # Filters
        print("Получить все категории с названием Медведь")
        print(Category.objects.filter(name="Медведь"))

        print("Получить все категории у которых название не Медведь")
        print(Category.objects.exclude(name="Медведь"))

        print("Получить все категории Медведь у которых имя не Тигр")
        print(Category.objects.filter(name="Медведь").exclude(name="Тигр"))

        print("Получить всех Животных с возрастом 10 лет")
        print(Animal.objects.filter(age=10))

        print("Получить всех Животных с возрастом более 10 лет")
        print(
            f"{Animal.objects.filter(age__gt=10)}, количество {Animal.objects.filter(age__gt=10).count()}"
        )

        print("Больше 10 и меньше 20 лет")
        print(Animal.objects.filter(age__gt=10, age__lt=20).count())

        print("Получить категорию, которая начинается на <Ч>")
        print(Category.objects.filter(name__startswith="Ч"))

        print("Получить категорию, которая содержит <ee>")
        print("Все категории")
        print(Category.objects.all())
        print(Category.objects.filter(name__icontains="е"))

        print("Получить всех Медведей")
        bears = Category.objects.get(name="Медведь")
        print(Animal.objects.filter(category=bears))
        # Тоже самое:
        print(Animal.objects.filter(category__name="Медведь"))

        print("Получить всех животных у которых имя категории начинается на <Ч>")
        print(Animal.objects.filter(category__name__startswith="Ч"))
