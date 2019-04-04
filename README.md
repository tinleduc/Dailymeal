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
    

Step 20: create templates menu/Ingredientcount.html

    <h1>{{ food.food_name }}</h1>
    
    <ul>
    {% for ingredient in ingredient.Foodingredient_set.all %}
        <li>{{ ingredient.ingredient_name }} -- {{ ingredient.ingredientcount }} vote{{ ingredient.ingredientcount|pluralize }}</li>
    {% endfor %}
    </ul>
    
    <a href="{% url 'menu:ingredient' food.id %}">Vote again?</a>

Step 21: Use generic views: Less code is better

    These views represent a common case of basic Web development: 
getting data from the database according to parameter passed in the URL
loading a template and returning the rendered template
Because this is so commom Django provides a shortcut called the generic views system

Generic views abstract common patterns to the point where you don't even need to write python code to write app
Let convert our poll app to use the generic view system 
1. Convert the URLconf
2. Delete some of the old unneeded views
3. Introduce new views based on Django's genenric views


Step 22: Amend - make minor change in (a text)  in order to make it fairer more accurate or more up-to date URLconf
Firts, open the polls/urls.py and change it like

    from django.urls import path
    
    from . import views
    
    app_name = 'menu'
    urlpatterns = [
        path('', views.MenuView.as_view(), name='menu'),
        path('<int:pk>/', views.FoodsView.as_view(), name='food'),
        path('<int:pk>/ingredient/', views.IngredientsView.as_view(), name='ingredient'),
        path('<int:food_name>/ingredient/count', views.ingredientcount, name='ingredientcount'),
    ]
Step 23: Amend views
    Next we're going to remove our old menu, food, and results views and use Django's generic views instead
    Open menu/views.py file and change it
    
        from django.http import HttpResponseRedirect
        from django.shortcuts import get_object_or_404, render
        from django.urls import reverse
        from django.views import generic
        
        from .models import Food, Ingredient
        
        
        class MenuView(generic.ListView):
            template_name = 'menu/menu.html'
            context_object_name = 'latest_food_list'
        
            def get_queryset(self):
                """Return the last five published questions."""
                return Question.objects.order_by('-pub_date')[:5]
        
        
        class FoodlView(generic.DetailView):
            model = Food
            template_name = 'menu/fooddetail.html'
        
    In this case we use two generic views here: ListView and DetailView. 
    Respectively, those two views abstract the concepts of display a list of objects 
    and display a detail page for a particular type of object

    Each generic view needs to know what model it will be acting upon.
    This is provided using the model attribute

    The DetailView generic  view expects the primary key value captured from the URL to be called pk
    so we changed question_is to pk for the generic views

    By default, the DetailView generic  view uses the template call <app_name> <model_name>_detail.html
    In our case it would use the template menu/fooddetail.html
    The template_name attribute is used to tell Django to use a specific template name instead of the auogenerated
    default template name. We also specify the template name for the Ingredient list view this ensures that 
    the Ingredients views and the Food view have a different apperance when rendered 
    even though they're both  a DetailView behind the scenes
    
    Similarly, the ListView generic view uses a default template called app_name/model_name_list.html
    


Step 24: Introducing automated testing

What are automated tests?
Test are simple routes that check the operation of your code

Why you need to create tests

    Tests will save you time
    Tests don't just identify problems, the prevent them
    Tests make your code more attractive
    Tests help teams work together

Basic testing strategies

Writing our first test

    We identify a bug
    Create a test to expose the bug
    Running tests
    Fixing the bug
    More comprehensive tests

Test a view

    A test for a view
    The Django test client
    Improving our view
    Testing our new view
    Testing the DetailView
    Ideas for more tests

When testing more is better

Futher testing

What's next

Step 25: Customize your app's look and feel

Step 26: Adding a background-image

Step 27: Customize the admin form

Step 28: Adding the related objects

Step 29: Customize the admin change list

Step 30: Customize the admin look and feel
    Customize your projects's templates
    Customize your application's templates
    
Step 31: Customize the admin index page
What's next

Step 32: How to write reused apps
    
    Reusability matters
    
        Reusability is the way of life in PYthon
        The Python Package Index (PyPI) has a vast range of packages you can use in your own Python programs.
        Check out Django Packages for existing reusable apps you could incorporate in your project
        Django itself is also just a Python Package
        This meams you can take existing python Packages or Django apps and compose them into your own web project
        You only to write the parts that make your project unique
            
            Note: Package and App
            A Python package provide a way of grouping related Python code for easy reuse
            A package contians one or more files of Python code (modules)
            A package can be imported with
                import ... 
                or
                from .. import
            For a directory to form a package, it must contain a special file __init__.py
            even if this file is empty
            
            Django Application is just a Python Package that is specifically intended for use in Django project
            An Application may use common Django conventions such as having models, tests, urls, and views submodules
            
            Later on we use the term packaging to describe the process of making a pythong Package easy for other to install 
            It can be a little confusing we know
            
    Your project and your reusable app
    Install some prerequisites
        
        The current state of Python packaging is a bit muddled with various tools.
        For this tutorial, we're going to use setuptools to build our package.
            
            pip install setuptools
            
                Note: is a fully-featured actively-maintained and stable library designed to facilitate package Python  
                projects where packaging includes:
                    Python package and module definitions
                    Distribution package metadata
                    Test hooks
                    Project installation
                    Paltform-specific detail
                    Python 3 support                             
            
        It's the recommended packaging tool
        We'll also be using pip to install and uninstall it
            
            pip install Django 
    
    Packaging your app
    Refers: https://packaging.python.org/tutorials/packaging-projects/
        Python packaging refers to preparing your app in a specific format that can be easily installed and used.
            1/ First, create a parent directory for project, outside of your Django project. Call this directory Django-project
            2/ Move the project directory into Django-project
            3/ Create a file django-polls/README.rst with content:
                =====
                Projects
                =====
                
                Projects is a simple Django app to conduct Web-based Projects. For each
                Projects_content, visitors can choose between a fixed number of answers.
                
                Detailed documentation is in the "docs" directory.
                
                Quick start
                -----------
                
                1. Add "Projects_content" to your INSTALLED_APPS setting like this::
                
                    INSTALLED_APPS = [
                        ...
                        'Projects',
                    ]
                
                2. Include the Projects URLconf in your project urls.py like this::
                
                    path('Projects/', include('Projects.urls')),
                
                3. Run `python manage.py migrate` to create the Projects models.
                
                4. Start the development server and visit http://127.0.0.1:8000/admin/
                   to create a Projects (you'll need the Admin app enabled).
                
                5. Visit http://127.0.0.1:8000/polls/ to participate in the Projects.
            4/ Create a django-projects/LICENSE file
            Choosing a license is beyond the scope of this tutorial but suffice 
            it to say that code released publicly without a license is useless. Django and
            many Django-compatible apps are distibuted under the BSD license
            5/ Next we create a setup.py file which provides details about how to build and install app.
            A full explanation of this file is beyond the scope of this tutorial bu the setuptools docs have a good explanation
            Create a file django-polls/setup.py with the following contents:
                
                import os
                from setuptools import find_packages, setup
                
                with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
                    README = readme.read()
                
                # allow setup.py to be run from any path
                os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
                
                setup(
                    name='django-polls',
                    version='0.1',
                    packages=find_packages(),
                    include_package_data=True,
                    license='BSD License',  # example license
                    description='A simple Django app to conduct Web-based polls.',
                    long_description=README,
                    url='https://www.example.com/',
                    author='Your Name',
                    author_email='yourname@example.com',
                    classifiers=[
                        'Environment :: Web Environment',
                        'Framework :: Django',
                        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: BSD License',  # example license
                        'Operating System :: OS Independent',
                        'Programming Language :: Python',
                        'Programming Language :: Python :: 3.5',
                        'Programming Language :: Python :: 3.6',
                        'Topic :: Internet :: WWW/HTTP',
                        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                    ],
                )
            6/ Create a MANIFEST.in file
            The setuptoold docs referred to in the previous step discuss this file in more details
            To include the templates the README.rst and our LICENSA file 
            create a file django-polls/MANIFEST.in with following content:
                
                include LICENSE
                include README.rst
                recursive-include polls/static *
                recursive-include polls/templates *
            
            7/ It's optional but recommended , to include detail documentation with your app
            Create an empty directory django-pools/docs for future documentation
            Add an additional line to MANIFEST.in
            
                recursive-include docs *
             
            8/ Try building your package with - run from inside django-project directory
                
                python setup.py sdist 
                
                This creates a directory called dist and builfs your new package,
                django-projects-0.1.tar.gz.
                
    Using your own package
        
        Since we moved the projects directory out of project it no longer working
        We'll fix this by installing our new django-project package
           Installing as a user library
             Per-user installs have alot of advantages over installing the package system-wide 
             such as being  usable on systems where you don't have administrator access 
             as well as preventing the package from affecting system services and other users of machine
             
         1/ Install the package use pip
         pip install --user django-projects/dist/django-projects-0.1.tar.gz
         
         2/ With luck your django project should now work correctly again
         Run the server agian to confirm this
         
         3/ To Uninstall the package use pip
         
            pip uninstall django-projects
            
    Publishing your app
         Your app is ready to share with the world
         
            Email the package to a friend
            Upload the package on your website
            Post the package on a public repository such as PyPI
            packaging.python.org
            
    Installing Python packages with virtualenv
         
Step 33: What to read next

    Finding documentation    
    How the documentation is organized
        Django's main documentation is broken up to into chunks designed to fill different needs
            - The introductoty material is designed for people new to django
            - The Topic guides on the other hands, dive deep into individual parts of django 
            There are complete guides to Django's model system, template engine, forms framework and much more
            - Web development is often broad not deep - problems span many domains- 
            include set of how-to guides that answers common How do I
            - It don't cover every signle class function and method avaiable in Django
            - Have several guides for various deployment setups as well as deployment checklist for some things
            
        
    How documentation is updated
    Where to get it 
        On the Web
        In Plain text
        As HTML locally
    Differences between version
    
Step 34: Writing your first patch for Django
    
    Introduction
        
        Interested in giving back to the community a little? 
        Maybe you found a bug in Django that you like to see fixed, 
        or maybe there's a small feature you want added
        
        Contributing back to Django itself is the best way to see your own concerns addressed
        This may seem daunting at first but it really prettry simple.        
    
    Code of Conduct
        https://www.djangoproject.com/conduct/
    
    Installing Git
        https://git-scm.com/download
    
    Getting a copy of Django's development version
         - fork Django on Github
         - navigate to the directory where you'll want yourlocal copy of Django to live
            git clone git@github.com:YourGitHubName/django.git
        Now you have local copy of Django you can install it just like you would install any package using Pip
        It's good idea to keep all your virtual enviroment in one place for example in .virtaulens/
        
        Create a new virtual envirment by running
            python3 -m venv ~/.virtualenvs/djangodev
        
        The  path is where the new enviroment will be saved on your computer
        The final step in setting up your virtual environment is to acitvate it
        
            source ~/.virtualenvs/djangodev/bin/activate
            
            For Window users
            
            ...\>
            %HOMEPATH%\.virtualenvs\djangodev\Scripts\activate.bat
            
            --> The name of the currently activated virtual environment is displayed on the command line 
            to help we track of which one your are using.
            
            Anything you install through pip while this name is displayed 
            will installed in that virtual environment, isolated from other environments and systems-wide packages
            
            Install the previously clone copy of django
            
            pip install -e /path/to/your/local/clone/django/
            
    Running Django's test suit for the firt time
        When contributing to Django it's very important that 
        your code changes don't introduce bugs into other areas of Django
        One way make sure: running Django's test suite.
        
        Before running the test suite, install its dependencies by cd-ing 
        into django tests/directory and then running
            pip install -r requirements/py3.txt
            
            
    Working on a feature
    Creating a branch for your patch
    Writing some test for your ticket
        Writing a test for ticket #99999
        Running your new test
    Writing the code for your ticket
    Running Django's test suite for the second time
    Writing Documentation
    Previewing your changes
    Committing the changes in the patch
    Pushing the commit and making a pull request
    Next steps:
        More information for new contributors
        Find your first real ticket
        What's next after create a pull request
            
  
Step 35: Using Django
        
    How to install Django
        Install Python
        Install Apache and mod_wsgi
            Django includes a lightweight web server you can use for testing
            so you won't need to set up Apache until you're ready to deploy Django in production
            If you want use Django on productin site, use Apache with mod_wsgi
            mod_wsgi operates in one of two modes, embedded mode or daemon mode
            embedded_mode: mod_wsgi is similar to mod_perl it embeds Python within Apache 
            and loads Python code into memory
            
            How to use Django with Apache and mod_wsgi
            https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/            
            
        Get your database running
            if you plan to use Django's Database API functionality, you make sure a database server is running
            Django support many different database servers and
             is officially supported with PostgreSQL MySQL Oracle SQLite
             
             If you are developing a simple project or somthing you don't plan to deploy in a production
             environment SQLite is generally the simplest option as it doesn't require running a separate server
             
             In addition to the officially supported database, 
             there are backend provided by 3rd parties that allow you to use other databases with Django
                PostgreSQL
                    https://docs.djangoproject.com/en/2.1/ref/databases/#postgresql-notes
                MySQL
                    https://docs.djangoproject.com/en/2.1/ref/databases/#mysql-notes
            If you plan to use Django'manage.py migrate command to automatically create database tables 
            for your models, you need to ensure that 
            Django have permission to create and alter tables in the database you're use
            If you plan to manually create the tables you can simply grant Django 
            SELECT, INSERT UPDATE and DELETE permission
            
            IF you're using Django's testing framework to test database queries , 
            Django will need permission to create a test database      
             
        Install the Django Code
    
    Models and databases
        Models
            Overview
                is the single, definitive source of information about your data.
                It contains the sesential fields and behaviors of the data you storing.
                Generally, each model maps to a single datable table
                Note:
                    Each model is a Python class that subclasses django.db.models.Model
                    Each attribute of the model represents a database field
                    With all of this Django gives you an automatically database-access API
                Notes:
                    The name of table is automatically derived from some models metadata but can ve overridden
                    An id field is added automatically but this behavior can be overridden
            Using models
                You need to tell Django you going to use models which you have defined
                By editing your settings file and changing the INSTALLED_APPS setting 
                to add the name of module that contains your models.py
            Fields
                The most important part of a model and the only required part of model
                 - is list of database fields it defines
                Fields are specified by class attributes.
                Field types
                Field options
                Automatic primary key fields
                Verbose field names
                Relationships
                    Many-to-many Relationships
                    Extra fields on many-to-many Relationships
                    One-to-one relationships
                Models across files                
                Field name retrictions                
                Custome field type           
            Meta Options            
            Models attributes                
            Model methods                
                Overrideing predefined model methods                
                Executing custome SQL                
            Model inhertance                
                Abstrach base classes                
                    Meta inheritance
                    Becareful with related_name and related_query_name                
                Multi-table inheritance                
                    Meta and multi-table inheritance                    
                    Inheritance and reverse relations                    
                    Specifying the parent link field                
                Proxy models                
                    QuerySet still return the model that was requested
                    Base class restrictions
                    Proxy model managers
                    Differences between proxy inheritance and unmanaged models                
                Multiple inheritance                
                Field name hiding is not permitted                
            Organizing models in a package
                             
        Making queries
            Creating objects
            Saving changes to objects
                Saving ForeignKey and ManyToManyFields fields
            Retrieving objects 
                Retrieving all objects
                Retrieving specific objects with filters
                Filtered QuerySets are unique
                QuerySet are lazy
            Retrieving a single object with get
            Other QuerySet methods
            Limiting QuerySets
            Field lookups
            Lookups that span relationships
                Spanning multi-valued relationships
            Filters can reference fields on the model
            The pk lookup shortcut
            Escaping percent signs and underscores in LIKE statements
            Caching and QuerySets 
                When QurerySet are not cached
            Complex lookups with Q objects
            Comparing objects
            Deleting objects
            Copying model instances
            Updating multiple objects at once
            Related Objects 
                One to many relationship    
                    Forward
                    Following realationships backward
                    Using a custom reverse manager
                    Additional methods to handle related objects
                Many to many relationships
                One to one relationships
                How are the backward relationships possible
                Queries over related objects
            Falling back to raw SQL
             
        Aggregations
        Search
        Managers
        Performing raw SQL queries
        Database transactions
        Muiltiple databases
        Tablespaces
        Database access optimization
        Database instrumentation
        Examples of model relationship API usage        
    
    Handling HTTP requests
        URL dispatcher
        Writing views
        View decorators
        File Upload
        Django shorcut functions
        Generic views
        Middleware
        How to use sessions
    
    Working with forms
        HTML forms
        Django'role in forms
        Forms in Django
        Building a form
        More about Django Form classes
        Working with form templates
        Futher topics
    
    Templates
        Support for template engines
        The Django template language
    
    Class-based Views
        Introduction to class-based views
        Buil-in class-based generic views
        Form handling with class-based views
        Using mixins with class-based views
        Basic examples
        Simple usage in your URLconf
        Subclassing generic views
            
    Migrations
        The commands
        Backend support
        Workflow
        Dependencies
        Migration files
        Adding migrations to apps
        Historical models
        Consideration when removing model fields
        Data Migrations
        Squashing migrations
        Serializing values
        Supporting multiple Django version        
        
    Managing files
        Using file in models
        The file object
        File storage
    
    Testing in Django
        Writing and running tests
        Testing tools
        Advanced testing topic
    
    User authentication in Django
        Overview
        Installation
        Usage    
    
    Django'cache framework
         Setting up the cache
         The per-site cache
         Template fragment caching
         The low-level cache API
         Downstream caches
         Using vary headers
         Controlling cache: Using other headers
         Order of MIDDLEWARE
    
    Conditional View Processing
        The condition decorator
        Shortcuts for only computing one value
        Using the decorator with other HTTP methods
        Comparision with middleware conditional processing
    
    Cryptographic signing
        Protecting the SECRET_KEY
        Using the low-level API
    
    Sending email
        Quick example
        send_mail()
        send_mass_mail()
        mail_admins()
        mail_managers()
        Examples
        Preventing Header injection
        The EmailMessage class
        Email backend
        Configuring email for development
    
    Internationalization and localozation
    
    Logging
    
    Pagination
    
    Security in Django
    
    Performance and optimization
    
    Serialization Django objects
    
    Django settings
    
    Signals
    
    Systemcheck framework
    
    External Packages
    
    
    

Step 36:
Step 37:
Step 38:
Step 39:
Step 40:
Step 41:
Step 42:
Step 43:
Step 44:
Step 45:
Step 46:
Step 47:
Step 48:
Step 49:



