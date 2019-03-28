from django.urls import path

from . import views

urlpatterns = [
    # /menu/
    path('', views.menu, name='menu'),
    # /menu/food/
    path('food/', views.food, name='food'),
    # /menu/food/food_name/
    path('food/<food_name>/', views.fooddetail, name='fooddetail'),
    # /ingredient list/
    path('ingredient/', views.ingredient, name='ingredient'),
    # /ingredient/ingredient_name/
    path('ingredient/<str:ingredient_name>/', views.ingredientdetail, name='ingredientdetail'),
    # /ingredient/ingredient_name/count/
    path('ingredient/<str:ingredient_name>/count', views.ingredientcount, name='ingredientcount'),
]


