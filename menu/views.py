from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import *

# Create your views here.


def food(request):
    lastest_food_list = Food.objects.order_by('-created_at')[:5]
    # template = loader.get_template('menu/food.html')
    context = {'lastest_food_list':lastest_food_list,}
    # return HttpResponse(template.render(context,request))
    return render(request, 'menu/food.html', context)


# def fooddetail(request, food_name):
#     try:
#         food = Food.objects.get(food_name=food_name)
#     except food.DoesNotExit:
#         raise Http404("Food does not exist")
#     return render(request, 'menu/fooddetail.html', {'food': food})


def fooddetail(request, food_name):
    food = get_object_or_404(Food, food_name=food_name)
    return render(request, 'menu/fooddetail.html', {'food': food})


# def foodcount(request, food_name):
#     food = get_object_or_404(Food, food_name=food_name)
#     try:
#         selected_food = Food.Inredient
#     ingredient = get_object_or_404(Ingredient, ingredient_name=ingredient_name)
#     return render(request, 'menu/ingredientdetail.html', {'ingredient': ingredient})


def ingredient(request):
    lastest_ingredient_list = Ingredient.objects.order_by('-created_at')[:3]
    context = {'lastest_ingredient_list': lastest_ingredient_list}
    return render(request, 'menu/ingredient.html', context)


def ingredientdetail(request, ingredient_name):
    ingredient = get_object_or_404(Ingredient, ingredient_name=ingredient_name)
    return render(request, 'menu/ingredientdetail.html', {'ingredient': ingredient})


def ingredientcount(request, food_name):
    food = get_object_or_404(Food, food_name=food_name)
    try:
        selected_ingredient = food.foodingredient_set.get(pk=request.POST['ingredient'])
    except (KeyError, Ingredient.DoesNotExist):
        return render(request, 'menu/fooddetail.html',
                      {'food': food,
                       'error_message': "You did not sellect a igredient"
                        })
    else:
        selected_ingredient.ingredient_name += 1
        selected_ingredient.save()
    return HttpResponseRedirect(reverse('menu/<str:ingredient_name>/results/', args=(food_name)))


def meal(request, meal_name):
    return HttpResponse("You're looking at %s." % meal_name)











