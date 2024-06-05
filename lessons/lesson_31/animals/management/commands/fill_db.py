import random
from django.core.management.base import BaseCommand
from animals.models import Category, Animal, Food


class Command(BaseCommand):
    def handle(self, *args, **options):
        # здесь мы можем писать любые скрипты, связанные с проектом
        print("Filling db ...")
        # 1. Удаление
        Category.objects.all().delete()

        # 2. Создание
        bear = Category.objects.create(name="Медведь Неправильный")

        # 3. Изменение
        bear.name = "Медведь"
        bear.save()  # делаем только тогда, когда что-то изменили в базе

        tiger = Category.objects.create(
            name="Тигр",
        )

        turtle = Category.objects.create(
            name="Черепаха",
        )

        # также можно использовать такой подход для создания данных в базе
        # turtle = Category(
        #     name="Черепаха",
        # )
        #
        # turtle.save()

        category_list = [
            bear,
            tiger,
            turtle,
        ]

        # 4. Все данные
        print(Category.objects.all())

        Animal.objects.all().delete()

        # 5. Получить только 1 объект
        # bear = Category.objects.get(id=bear.id)  # если известно
        # bear = Category.objects.get(name="Медведь")  # по имени
        ANIMAL_COUNT = 1000

        animals_to_create = []

        for i in range(ANIMAL_COUNT):
            random_category = random.choice(category_list)
            # добавляем объекты в оперативную память
            animal = Animal(
                name=f"animal_{i}",
                category=random_category,
                age=random.randint(1, 20),
            )
            animals_to_create.append(animal)

        Animal.objects.bulk_create(animals_to_create)

        print(Animal.objects.all().count())
        print("Done")

        food_names = [
            "Банан",
            "Мясо",
            "Яблоко",
            "Мед",
            "Рыба",
        ]

        Food.objects.all().delete()

        for name in food_names:
            Food.objects.create(
                name=name,
            )
        print(Food.objects.all().count())

        all_animals = Animal.objects.all()

        for animal in all_animals:
            food_count = random.randint(1, 5)
            random_food_names = random.sample(food_names, food_count)

            for name in random_food_names:
                random_food = Food.objects.get(name=name)
                # Many to many save
                animal.food.add(random_food)
            animal.save()
