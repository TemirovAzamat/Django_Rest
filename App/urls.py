from django.urls import path

from .views import category_list_create_api_view, product_list_create_api_view

urlpatterns = [
    path('category/', category_list_create_api_view),
    path('product/', product_list_create_api_view)
]
