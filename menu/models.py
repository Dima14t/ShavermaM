from django.db import models

# Create your models here.



class Menu(models.Model):
    name =  models.CharField(max_length=150)   # Имя
    weight = models.FloatField()               # Вес
    price = models.DecimalField(max_digits=7, decimal_places=2)    # Цена1
    photo =  models.ImageField(upload_to= "menu/")    # Фото
    description =  models.TextField(null=True, blank=True)   # Описание
    сomposition =  models.TextField(null=True, blank=True)       # Ингидиенты
    rating =  models.FloatField()    # Рейтинг
    is_selling =  models.BooleanField(default=False)    # В продаже ?



    def __str__(self):
        return self.name
