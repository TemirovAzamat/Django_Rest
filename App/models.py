from django.db import models as m


class Category(m.Model):
    name = m.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(m.Model):
    name = m.CharField(max_length=30)
    price = m.IntegerField()
    category = m.ForeignKey(Category, on_delete=m.CASCADE)

    def __str__(self):
        return self.name

