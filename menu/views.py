from django.views.generic import TemplateView, FormView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.forms import  ValidationError
import csv
from django.contrib.auth.models import User

from .models import *
from .forms import *
# Create your views here.


class HomepageView(TemplateView):
    template_name = 'adminpages/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            context['lastest_food_list'] = Food.objects.order_by('-created_at')[:5]
            context['lastest_ingredient_list'] = Ingredient.objects.order_by('-created_at')[:5]
        else:
            context['lastest_food_list'] = Food.objects.order_by('-created_at')[:1]
            context['lastest_ingredient_list'] = Ingredient.objects.order_by('-created_at')[:1]
        return context


class LoginView(FormView):
    template_name = 'adminpages/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # User authenticated
            return redirect('homepage')
        return render(self.request, 'adminpages/login.html')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is None:
            form.add_error(None, ValidationError('The username or password is incorrect'))
            return self.form_invalid(form)

        login(self.request, user)
        # Redirect to a success page.
        return redirect('homepage')


def logout_view(request):
    logout(request)
    return redirect('homepage')


class RegisterView(TemplateView):
    template_name = 'adminpages/register.html'

#
# def menu(request):
#     lastest_food_list = Food.objects.order_by('-created_at')[:5]
#     # template = loader.get_template('menu/food.html')
#     context = {'lastest_food_list':lastest_food_list,}
#     # return HttpResponse(template.render(context,request))
#     return render(request, 'menu/food.html', context)
#
#     lastest_ingredient_list = Ingredient.objects.order_by('-created_at')[:3]
#     context = {'lastest_ingredient_list': lastest_ingredient_list}
#     return render(request, 'menu/ingredient.html', context)


class AllFoodView(ListView):
    template_name = 'menu/foodlist.html'
    context_object_name = 'lastest_food_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Food.objects.order_by('-created_at')
        else:
            return Food.objects.order_by('-created_at')[:1]


class FoodListView(ListView):
    template_name = 'menu/food.html'
    context_object_name = 'best_food_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Food.objects.order_by('-created_at')[:5]
        else:
            return Food.objects.order_by('-created_at')[:1]
#
#
# def food(request):
#     lastest_food_list = Food.objects.order_by('-created_at')[:5]
#     # template = loader.get_template('menu/food.html')
#     context = {'lastest_food_list': lastest_food_list}
#     comments = Comment.objects.all()
#     # return HttpResponse(template.render(context,request))
#     return render(request, 'menu/food.html', context)


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

        messages.success(request, '{} votes: {}'.format(ingredient_count.ingredient_name, ingredient_count.ingredient_count))
        return HttpResponseRedirect(reverse('fooddetail', kwargs={'food_name': food_name}))


def add_comment_to_food(request, food_name):
    food = get_object_or_404(Food, food_name=food_name)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.food = request.food
            comment.user = request.user
            comment.save()
            return redirect('fooddetail', food_name=food.food_name)
    else:
        form = CommentForm()
    return render(request, 'menu/add_comment_to_food.html', {'form': form})


class AllIngredientView(ListView):
    template_name = 'menu/ingredientlist.html'
    context_object_name = 'lastest_ingredient_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Ingredient.objects.order_by('created_at')
        else:
            return Ingredient.objects.order_by('created_at')[:1]


class IngredientListView(ListView):
    template_name = 'menu/ingredient.html'
    context_object_name = 'best_ingredient_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Ingredient.objects.order_by('created_at')[:5]
        else:
            return Ingredient.objects.order_by('created_at')[:1]
#
#
# def ingredient(request):
#     lastest_ingredient_list = Ingredient.objects.order_by('-created_at')[:3]
#     context = {'lastest_ingredient_list': lastest_ingredient_list}
#     return render(request, 'menu/ingredient.html', context)


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
    return HttpResponseRedirect(reverse('menu/ingredient/<str:ingredient_name>/count', args=ingredient_name))


def countresult(request, food_name):
    food = get_object_or_404(Food, food_name=food_name)
    return render(request, 'menu/ingredientcount.html', {'food': food})


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response


def export_food_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="food.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Food', 'Description'])

    foods = Food.objects.all().values_list('id', 'food_name', 'food_des')
    for food in foods:
        writer.writerow(food)

    return response









