from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from .models import *

# Create your views here.


def menu(request):
    lastest_food_list = Food.objects.order_by('-created_at')[:5]
    # template = loader.get_template('menu/food.html')
    context = {'lastest_food_list':lastest_food_list,}
    # return HttpResponse(template.render(context,request))
    return render(request, 'menu/food.html', context)

    lastest_ingredient_list = Ingredient.objects.order_by('-created_at')[:3]
    context = {'lastest_ingredient_list': lastest_ingredient_list}
    return render(request, 'menu/ingredient.html', context)



def food(request):
    lastest_food_list = Food.objects.order_by('-created_at')[:5]
    # template = loader.get_template('menu/food.html')
    context = {'lastest_food_list':lastest_food_list,}
    # return HttpResponse(template.render(context,request))
    return render(request, 'menu/food.html', context)


def fooddetail(request, food_name):
    if request.method == 'GET':
        food = get_object_or_404(Food, food_name=food_name)
        return render(request, 'menu/fooddetail.html', {'food': food})
    elif request.method == 'POST':
        ingredient_name = request.POST.get('ingredient')
        ingredient = Ingredient.objects.get(ingredient_name=ingredient_name)
        ingredient_count, created = Ingredientcount.objects.get_or_create(ingredient_name_id=ingredient.id, defaults={
            'ingredient_count': 0,
            'ingredient_count_des': ingredient_name
        })
        ingredient_count.ingredient_count += 1
        ingredient_count.save()

        messages.success(request, 'ingredient_count: {}'.format(ingredient_count.ingredient_count))
        return HttpResponseRedirect(reverse('fooddetail', kwargs={'food_name': food_name}))


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
    return HttpResponseRedirect(reverse('menu/ingredient/<str:ingredient_name>/count', args=(ingredient_name)))


def countresult(request, food_name):
    food = get_object_or_404(Food, food_name=food_name)
    return render(request, 'menu/ingredientcount.html', {'food': food})












