Step 01: Create project dailymeal

Step 02: Create app meanu

Step 03: Create simple Homepage
    urls.py (project) --> urls.py(app) --> views.py(app)

Step 04: Migrate 

Step 05: Runserver --> view Homepage

Step 06: Setting.py Database setup + Change timezone + Add Installed app 

Step 07: Create model

1/ Region # Subregion # Countrycategory #  Country # District # Ward # Street # Address 
- define location of user


2/ Unit #
Define unit use in project


3/ Jobcategory # Job # Relation # Agecategory # Weightcategory # Bloodpressurecategory # Heartbeatcategory # Healthstatus

Define factor effect enegy consumption of Object and other information make realtions


4/ ObjectConsume 

Create information of models (Object's enegy consumption classify by above factor) 

5/ Host # Familymember 

# Define input information of user

6/ Memberconsume # Familyconsume

# Define result level 1 of inmput infor - the enegy of each member need per day  and total of all member

7/ Foodcategory # Foodingredient

# Define classify of food we eat and the ingredients of them, caculate in unit

8/ Balancemeal # Dailymeal # Dailyfamilyconsume

# Define the standard of dailymeal for family based on the total consumption of family and standard meal for normal person.

9/ Menusuggest

# Caculate and suggest menu based on standard meal - foodingredient and time of request.

10/ Menuhistory # MenuActual

# Save infor of history and input infor of user # Use this infor for next proccess suggest menu

11/ Expand function:

+ Suggest cong thuc nau an (dua tren thuc pham chon, thoi tiet, lich su an uong )
+ Bo sung gia vi theo cong thuc nau an da chon
+ Suggest dia diem ban hang dap ung nhu cau gan do
+ Du tinh chi phi dua tren gia ca cac mat hang.
+ Tich hop mua hang online (Vinmart++)


12/ Basic function

Suggest menu/thuc don dua vao thong tin

+ Dia diem
+ So luong nguoi
+ Hinh thuc tiec
+ ...

Step 08: 

Add Installed_apps
    "menu.apps.MenuConfig"

Run: python manage.py makemigrations menu 
# telling Django that we made some changes to our models 
# and that we like the changes to be stored as migration
 
    Migrations for 'menu':
      menu/migrations/0001_initial.py:
        - Create model ....
        - Create model ....
        ....
        - Add field .... to .....
        

Run: python manage.py sqlmigrate menu 0001
# To show what SQL that migration would run 
    BEGIN;
    --
    -- Create model ...
    --
    CREATE TABLE '...' (
    
    );
    --
    -- Create model ...
    --
    ...
    COMMIT;

Run: python manage.py migrate 

    Operations to perform:
        Apply all migrations: admin, auth, contentypes, menu, sessions
    Running migrations:
        Rendering model states ... DONE
        Applying menu.0001_initial...OK
        

Step 09: Introducing the Django admin

Createsuperuser -> Login Admin site 

Step 10: Make the menu app modifiable in the admin

Add admin.site.register(Model) in menul/admin.py

# Ordering apps in admin site.


Step 11: Writing more views

let add a fwe more view to menu/view.py
These views are slightly different because they take an argument.

Add path() in menu.urls

When user requests a page from your website - say /menu/moring_meal/
Django will load dailymeal.urls Python modules because it's pointed to by the ROOT_URLCONF setting.
It finds the variable name urlpatterns and traverses the patterns in order

There's no need to add URL cruft such as .html - unless you want to.


Step 12:  Write views that actually do something

Each view is responsible for doing one of two things return an HttpResponse
 
 Your view can read records from a database or not
 It can use a template system such as Django's or a third-party Python template system - or not.
 It can generate a PDF file output XML create a ZIP file on the fly anything you want, using whatever python libraries you want
 
 
 from django.http import HttpResponse
 from .model import Food 
 
 def index(request):
    lastest_food_list = Food.objects.order_by('-created_at')[:5]
    output = ', '.join([q.food_name for q in lastest_food_list])
    return HttpResponse(output)
 

Step 13:  Create template

There 's  a problem here : the page's design is hard coded in the view
If you want ro change the way page look, you'll have  to edit this python code 
so let use Django's template system to seperate the design from Python by creating a template that the view can use

* Create directory called templates in your menu directory
    By convention DjangoTemplates looks for a templates subdirectory in each of the INSTALLED_APPS

* Within the templates directory, create another directory called polls  and within that create a file  called index.html

    {% if lastest_food_list %}
        <ul>
        {% for food in lastest_food_list %}
            <li> <a href = "/pools/{{food.id}}/">{{food.food_name}}</a></li>
        {% endfor %}
    {% else %}
        <p> No polls are available. </p>
    {% endif %}   
* Update our index view in polls/views.py to use the template.

    from django.http import HttpResponse
    from django.template import loader
    from .model import Food 
         
         def index(request):
            lastest_food_list = Food.objects.order_by('-created_at')[:5]
            template = loader.get_template(menu/index.html)
            context = {'lastest_food_list':lastest_food_list,}
            return HttpResponse(template.render(context, request))
            
* A shortcut: render()

It's a very commom idiom to load a template fill a context a return an .

    from django.http import HttpResponse
    from django.template import loader
    from django.shortcuts import render
    from .model import Food 
         
         def index(request):
            lastest_food_list = Food.objects.order_by('-created_at')[:5]
            # template = loader.get_template(menu/index.html)
            context = {'lastest_food_list':lastest_food_list,}
            #return HttpResponse(template.render(context, request))
            return render(request, 'menu/index.html', context)
                     
Step 14: Raising a 404 Error

    from django.http import HttpResponse, Http404
    from django.template import loader
    from django.shortcuts import render
    from .model import Food 
    # ...
         
         def food(request, food_name):
            try:
                food = Food.objects.get(pk=food_name)
            except Food.DoesNotExit:
                raise Http404("Food does not exist")           
            return render(request, 'menu/food.html', {'food': food})
* Get objects or 404

    from django.http import HttpResponse, Http404
    from django.template import loader
    from django.shortcuts import render, get_objects_or_404
    from .model import Food 
    # ...
         
         def food(request, food_name):
            food = get_objects_or_404(Food, food_name=food_name)
            return render(request, 'menu/food.html', {'food': food})

Step 15: Use the template system 
    Back to the detail() view for our poll application
    Given the context variable question. here's what the polls/detail.html template might look like
        
        <h1> {{ food.food_name }} </h1>
        <ul>
        {% for ingredient in food.ingredient_set.all %}
            <li> {{ ingredient.ingredient_name}} </li>
        {% endfor %}
        </ul>
        

Step 16: Removing hardcode URLs in templates

Remember when we wrote the link to question the menu.index.html template the link was partially hardcoded like this:

<li><a href:"/menu/{{food_name}}/">{{food.food_name}}</a></li>

The problem with this hardcoded tightly-coupled approach is that 
it becomes challenging to change URLs on projects with a lot of templates.
However since you defined the name argument in th path() functions in the menu.urls modules
you can remove a reliance on specific URL paths defined in your configurations by using the {% URL %}
 temmplate tag:

    <li><a href = {% url 'food' food_name %}>{{food.food_name}}</a></li> 
    
    The way this works by looking up the URL definitions as specified in the menu.urls module.
    
    # The 'name' value as called by the {% URL %} template tag
    path('<str:food_name>/', views.food, name='food'),
    
Step 17: Namespacing URL names

In real Django projects there might many apps, to differentiate the URL names between apps, 
the answer is to add namespaces to your URLconf 

    from django.urls import path
    
    from . import views
    app_name = 'menu'
    
        urlpatterns = [
        # /menu/
        path('', views.index, name='index'),
        # /menu/meal_name/
        path('<str:meal_name>W/', views.meal, name='meal'),
        # /menu/food/
        path('<str:food_name>/', views.food, name='food'),
        
and change index.html

<li><a href = {% url 'menu:food' food_name %}>{{food.food_name}}</a></li> 

Step 18: Write a simple form

    <h1> {{ food.food_name }} </h1>
    {% if error_message %} <p><strong> {{error_message}}</strong></p>{% endif %}
    <form action="{% url 'fooddetail' food.id %}" method="post">
    {% csrf_token %}
    {% for ingredient in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
    <input type="submit" value="Vote">
    </form>

    Quick rundown:
    
    The above template displays a radio button for each food ingredient
    The value of each radio button is the associated question choices ID
    The name of each radio button is choice. That mean when somebody selects one of radio button is choice
    
    We set the form's action to {% url 'food:ingredient' food.food_name %} and we set method="post".
     Using method="post" (as opposed to method="get") is very important, 
     because the act of submitting this form will alter data server-side. 
     Whenever you create a form that alters data server-side, use method="post". 
     This tip isn’t specific to Django; it’s just good Web development practice.
     forloop.counter indicates how many times the for tag has gone through its loop
     Since we’re creating a POST form (which can have the effect of modifying data), 
     we need to worry about Cross Site Request Forgeries. 
     Thankfully, you don’t have to worry too hard, 
     because Django comes with a very easy-to-use system for protecting against it. 
     In short, all POST forms that are targeted at internal URLs should use the {% csrf_token %} template tag.
    
    
Step 19: Create a Django view that handles the submitted data and does something with it remember 

Add url menu/urls.py

path('ingredient/<str:ingredient_name>/count/', view.ingredientcount, name='ingredientcount')

Also created a dummpy implementation of the vote() function 
Let's create a real version add the following menu/view.py


        from django.http import HttpResponse, HttpResponseRedirect
        from django.shortcuts import get_object_or_404, render
        from django.urls import reverse
        
        from .models import Food, Ingredient
        # ...
        def IngredientCount(request, food_name):
            question = get_object_or_404(Food, pk=food_name)
            try:
                selected_foodingredient = Food.foodingredient.get(pk=request.POST['Ingredient'])
            except (KeyError, Ingredient.DoesNotExist):
                # Redisplay the question voting form.
                return render(request, 'menu/fooddetail.html', {
                    'food': food,
                    'error_message': "You didn't select a Ingredient.",
                })
            else:
                selected_foodingredient.votes += 1
                selected_foodingredient.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


Step 20:

Step 21:

Step 22:

Step 23:

Step 24:

Step 25:

Step 26:

Step 27:

Step 28:

Step 29:

Step 30:

Step 31: