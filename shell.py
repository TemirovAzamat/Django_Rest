from App.models import *

cat1 = Category.objects.create(name='Products')
cat2 = Category.objects.create(name='Soap washing')


prod1 = Product.objects.create(name='Bread', price=20, category=cat1)
prod2 = Product.objects.create(name='Water', price=45, category=cat1)
prod3 = Product.objects.create(name='Dish detergent', price=150, category=cat2)
prod4 = Product.objects.create(name='Powder', price=320, category=cat2)
prod5 = Product.objects.create(name='Shampoo', price=500, category=cat2)
