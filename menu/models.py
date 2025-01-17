from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')  # related_name qo'shildi

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=255)
    dishes = models.ManyToManyField(Dish, related_name='chefs')  # ManyToManyField uchun related_name qo‘shildi

    def __str__(self):
        return self.name
