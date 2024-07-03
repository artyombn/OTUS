# DJANGO - работа с пользователями и правами

- модель User
- регистрация и авторизация
- работа с текущим пользователем
- система прав Django


```python
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=18)
```
Setting (для использования своей модели User)  
`AUTH_USER_MODEL = 'users.MyUser'`  

