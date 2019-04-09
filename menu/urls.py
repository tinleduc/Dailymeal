from django.urls import path, include

from . import views

urlpatterns = [
    # Homepage
    path('', views.HomepageView.as_view(), name='homepage'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('exportusercsv/', views.export_users_csv, name='export_users_csv'),
    path('exportfoodcsv/', views.export_food_csv, name='export_food_csv'),
    # /menu/food/
    # path('food/', views.food, name='food'),

    # /menu/food/food_name/
    # all_food
    path('allfood/', views.AllFoodView.as_view(), name='allfood'),
    # food_list
    path('foodlist/', views.FoodListView.as_view(), name='foodlist'),
    # food_detail
    path('food/<food_name>/', views.fooddetail, name='fooddetail'),
    # add_comment_to_food
    path('food/<food_name>/comment/', views.add_comment_to_food, name='add_comment_to_food'),
    # /all_ingredient/
    path('allingredient/', views.AllIngredientView.as_view(), name='allingredient'),
    # /ingredient list/
    path('ingredientlist/', views.IngredientListView.as_view(), name='ingredientlist'),
    # /ingredient/ingredient_name/
    path('ingredient/<str:ingredient_name>/', views.ingredientdetail, name='ingredientdetail'),
    # /ingredient/ingredient_name/count/
    path('ingredient/<str:ingredient_name>/count', views.ingredientcount, name='ingredientcount'),
]


