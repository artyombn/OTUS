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
`forms.ModelForm`   # сразу связывается с моделью  
`forms.Form`   # если связь с моделью не нужна и нужно отправить простенькую форму  

Пример:
```python
from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = "__all__"
        # fields = ("name",) # можно указать только те поля, которые нужны
        # exclude = ("age",) # если хотим исключить только определенные поля
```
Для кастомизации полей:   
`name = forms.CharField(label="Имя животного", initial="default animal")`  

Можно добавить в форму виджет плейсхолдера:  
`widget=forms.TextInput(attrs={"placeholder": "Input Animal name"}),`

Чтобы сделать поле many-to-many не обязательным:  
`food = forms.ModelMultipleChoiceField(queryset=Food.objects.all(), required=False)`  




