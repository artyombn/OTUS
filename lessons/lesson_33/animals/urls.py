from django.urls import path, include
from animals import views

app_name = "animals"

urlpatterns = [
    path("", views.animals_list_view, name="index"),
    path("list/", views.AnimalListView.as_view(), name="list"),
    path("animal/<int:pk>/", views.AnimalDetailView.as_view(), name="detail"),
    # pk - ключ по которому будет искать
    path("create/", views.AnimalCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.AnimalUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.AnimalDeleteView.as_view(), name="delete"),
]
