from django.urls import path, include

from . import views

urlpatterns = [
    # Homepage
    path('', views.HomepageView.as_view(), name='homepage'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    # /menu/food/
    path('food/', views.food, name='food'),

    # /menu/food/food_name/
    path('food/<food_name>/', views.fooddetail, name='fooddetail'),
    path('food<food_name>/comment/', views.add_comment_to_food, name='add_comment_to_food'),
    # /ingredient list/
    path('ingredient/', views.ingredient, name='ingredient'),
    # /ingredient/ingredient_name/
    path('ingredient/<str:ingredient_name>/', views.ingredientdetail, name='ingredientdetail'),
    # /ingredient/ingredient_name/count/
    path('ingredient/<str:ingredient_name>/count', views.ingredientcount, name='ingredientcount'),
]


