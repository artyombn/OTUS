from django.db import models

# Create your models here.
# Связи, 1 к 1, 1 ко многим, многие ко многим:
# 1 - 1, 1 - *, * - *

# есть Медведь, имя Маша, еда - Мёд
# Тигр - Николай - Мясо
# Карточка животного (текст)


class Category(models.Model):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    age = models.PositiveBigIntegerField(default=0)
    food = models.ManyToManyField(Food)

    def __str__(self):
        # return self.name
        food_list = ", ".join([food.name for food in self.food.all()])
        return f"{self.name} -- {self.category.name} -- {self.age} -- {food_list}"


class Card(models.Model):
    text = models.TextField()
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
