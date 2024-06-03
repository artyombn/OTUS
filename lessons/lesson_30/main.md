# DJANGO

- познакомиться с Django
- научиться создавать проект и приложение
- научиться работать с базой данных

`python -m django startproject zoo .` - создание django проекта с именем zoo  
`python manage.py runserver` - запуск сервера  
`python manage.py startapp <name>` - создание нового приложение в проекте (новый модуль). создает базовую структуру каталогов и файлов, необходимых для работы приложения.  

**MVT - model & view & template**  
M - модели, связанные с БД  
V - обработчики запросов  
T - html страницы  

Связка 1 к 1:  
`animal = models.OneToOneField(Animal)`  

Связь 1 ко многим:  
`category=models.ForeignKey(Category, on_delete = models.CASCADE/PROTECT/SET_NULL)`  

Связи многие ко многим:  
`food = models.ManyToManyField(Food)`  


`python manage.py makemigrations` - создать миграцию  
`python manage.py migrate` - применить миграцию  

**_Создание админки:_**
`python manage.py createsuperuser`  

Для добавления моделей в админку:
```python
from .models import Category, Animal, Food, Card

# Register your models here.
admin.site.register(Category)
admin.site.register(Animal)
admin.site.register(Food)
admin.site.register(Card)
```

Для вывода команд через manage.py нужно использовать Django окружение
https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/
Cпециальные скрипты для выполнения различных задач в проекте через командную строку  
Являются частью инструментария Django для автоматизации и управления приложением  

Простые примеры основных запросов:
```python
        # 1. Удаление
        Category.objects.all().delete()

        # 2. Создание
        bear = Category.objects.create(name="Медведь Неправильный")

        # 3. Изменение
        bear.name = "Медведь"
        bear.save()

        # 4. Все данные
        print(Category.objects.all())
        print("Done")
```

