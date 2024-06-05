# DJANGO ORM, django-debug-toolbar

- научиться работать с Django ORM
- познакомиться с django-debug-toolbar

_https://django-debug-toolbar.readthedocs.io/en/latest/_


Получить все категории:
`Category.objects.all()`

### Filters, Exclude, 
Получить все категории с названием Медведь
`Category.objects.filter(name="Медведь")`

Получить все категории у которых название не Медведь
`Category.objects.exclude(name="Медведь")`

Получить все категории Медведь у которых имя не Тигр
`Category.objects.exclude(name="Медведь").exclude(name="Тигр")`

Получить всех Животных с возрастом 10 лет
`Animal.objects.filter(age=10)`

Получить всех Животных с возрастом более 10 лет
**_Нужно использовать модификаторы querysets:_**
https://docs.djangoproject.com/en/5.0/ref/models/querysets/
`Animal.objects.filter(age__gt=10)`

Больше примеров в get_animals.py


Оптимизация создания запросов через bulk_create()
```python
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
```
*Можно также использовать для Update


`animals = Animal.objects.all()` - обычный запрос

**Для оптимизации:**  
Чтобы подгрузить сразу связанные данные во избежание дубликатов запросов в БД
`animals = Animal.objects.select_related('category').all()`


`animals = Animal.objects.select_related("category").prefetch_related("food").all()`  
Для 1 к 1 или многие к 1: `select_related`  
Для многие ко многим: `prefetch_related`
