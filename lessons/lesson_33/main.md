# DJANGO Class Based Views, generics, Forms

- рассмотреть шаблоны для ускорения разработки
- познакомиться с формами


Для соединения установки папки templates, в которой будет происходить поиск шаблонов  
**в Settings.py**
```python
TEMPLATES = [
    {
        ...,
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        ...
    }
```

Классы View (CRUD): 
- ListView (R)
- DetailView (R)
- CreateView (C)
- UpdateView (U)
- DeleteView (D)
- FormView
- TemplateView


Пример для ListView:
```python
class AnimalListView(ListView):
    model = Animal
```

в ursl модели:
```python
urlpatterns = [
    path("", views.animals_list_view, name="index"),
    path("list/", views.AnimalListView.as_view(), name='list'),
]
```

Формы:
forms.ModelForm  # сразу связывается с моделью

