from django.db import models
from django.conf import settings


# Create your models here.


class Region(models.Model):
    region_name = models.CharField(max_length=50)
    region_symbol = models.CharField(max_length=20)
    region_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.region_name


class Subregion(models.Model):
    subregion_name = models.CharField(max_length=50)
    subregion_symbol = models.CharField(max_length=20)
    subregion_des = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subregion_name


class Countrycategory(models.Model):
    country_categoty_name = models.CharField(max_length=100)
    country_categoty_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_categoty


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.IntegerField()
    country_category = models.ForeignKey(Countrycategory, on_delete=models.CASCADE)
    subregion = models.ForeignKey(Subregion, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name


class Province(models.Model):
    province_name = models.CharField(max_length=50)
    province_code = models.IntegerField()
    province_des = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.province_name


class District(models.Model):
    district_name = models.CharField(max_length=50)
    district_code = models.IntegerField()
    district_des = models.TextField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.district_name


class Ward(models.Model):
    ward_name = models.CharField(max_length=50)
    ward_code = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ward_name


class Street(models.Model):
    street = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.street


class Address(models.Model):
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address


class Unit(models.Model):
    unit_name = models.CharField(max_length=50)
    unit_symbol = models.CharField(max_length=20)
    unit_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unit_name


class Relation(models.Model):
    relation_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.relation_name


class Jobcategory(models.Model):
    job_category_name = models.CharField(max_length=50)
    job_category_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_category_name


class Job(models.Model):
    job_name = models.CharField(max_length=50)
    job_category = models.ForeignKey(Jobcategory, on_delete=models.CASCADE)
    job_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_name


class Agecategory(models.Model):
    age_category_name = models.CharField(max_length=50)
    age_category_des = models.TextField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    age_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.age_category_name


class Weightcategory(models.Model):
    weight_category_name = models.CharField(max_length=50)
    min_weight = models.IntegerField()
    max_weight = models.IntegerField()
    weight_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.weight_category_name


class Bloodpressurecategory(models.Model):
    bloodpressure_category_name = models.CharField(max_length=50)
    bloodpressure_category_des = models.TextField()
    min_bloodpressure = models.IntegerField()
    max_bloodpressure = models.IntegerField()
    bloodpressure_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    age_category = models.ForeignKey(Agecategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.weight_category_name


class Heartbeatcategory(models.Model):
    heartbeat_category_name = models.CharField(max_length=50)
    heartbeat_category_des = models.TextField()
    heartbeat_category_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    min_heartbeat = models.IntegerField()
    max_heartbeat = models.IntegerField()
    age_category = models.ForeignKey(Agecategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.weight_category_name


class Healthstatus(models.Model):
    health_status_name = models.CharField(max_length=50)
    health_status_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.health_status_name


class Objectconsume(models.Model):
    object_name = models.CharField(max_length=200)
    object_des = models.TextField()
    object_gender = models.BooleanField()
    object_age_category = models.ForeignKey(Agecategory, on_delete=models.CASCADE)
    object_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    object_weight_category = models.ForeignKey(Weightcategory, on_delete=models.CASCADE)
    object_status = models.ForeignKey(Healthstatus, on_delete=models.CASCADE)
    object_consume = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.object_name


class Host(models.Model):
    host_name = models.CharField(max_length=200)
    host_gender = models.CharField(max_length=10)
    host_birthday = models.DateField()
    host_image = models.TextField()
    host_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    host_weight = models.IntegerField()
    host_height = models.IntegerField()
    host_bloodpressure = models.IntegerField()
    host_heartbeat = models.IntegerField()
    host_country = models.IntegerField()
    host_province = models.IntegerField()
    host_district = models.IntegerField()
    host_ward = models.IntegerField()
    host_street = models.CharField(max_length=200)
    host_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.host_name


class Familymember(models.Model):
    member_name = models.CharField(max_length=200)
    member_relation = models.ForeignKey(Relation, on_delete=models.CASCADE)
    member_gender = models.BooleanField()
    member_birthday = models.DateField()
    member_image = models.TextField()
    member_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    member_weight = models.IntegerField()
    member_height = models.IntegerField()
    member_bloodpressure = models.IntegerField()
    member_heartbeat = models.IntegerField()
    member_country = models.IntegerField()
    member_province = models.IntegerField()
    member_district = models.IntegerField()
    member_ward = models.IntegerField()
    member_street = models.CharField(max_length=200)
    member_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member_name


class Memberinfo(models.Model):
    member_consume_name = models.CharField(max_length=200)
    member_consume_enegy = models.IntegerField()
    member_age = models.IntegerField()
    member_age_category = models.CharField(max_length=100)
    member_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    member_job_category = models.ForeignKey(Jobcategory, on_delete=models.CASCADE)
    member_weight = models.IntegerField()
    member_weight_category = models.ForeignKey(Weightcategory, on_delete=models.CASCADE)
    member_height = models.IntegerField()
    member_bloodpressure = models.IntegerField()
    member_bloodpressure_category = models.CharField(max_length=200)
    member_heartbeat = models.IntegerField()
    member_heartbeat_category = models.CharField(max_length=200)
    member_country = models.IntegerField()
    member_province = models.IntegerField()
    member_district = models.IntegerField()
    member_ward = models.IntegerField()
    member_street = models.CharField(max_length=200)
    member_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member_name


class Familyconsume(models.Model):
    family_name = models.CharField(max_length=200)
    family_consume = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.family_name


class Foodcategory(models.Model):
    food_category_name = models.CharField(max_length=200)
    food_category_image = models.TextField()
    food_category_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_category_name


class Ingredientcategory(models.Model):
    ingredient_category_name = models.CharField(max_length=200)
    ingredient_category_image = models.TextField()
    ingredient_category_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient_category_name


class Ingredient(models.Model):
    ingredient_category = models.ForeignKey(Ingredientcategory, on_delete=models.CASCADE, default='')
    ingredient_name = models.CharField(max_length=200)
    ingredient_image = models.TextField()
    ingredient_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient_name


class Ingredientcount(models.Model):
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_count = models.IntegerField()
    ingredient_count_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient_name


class Food(models.Model):
    food_name = models.CharField(max_length=200)
    food_category = models.ForeignKey(Foodcategory, on_delete=models.CASCADE)
    food_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    food_image = models.TextField()
    food_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_name


class Foodchoice(models.Model):
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_choice = models.IntegerField()
    food_choice_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_name


class Foodenegy(models.Model):
    food_enegy_name = models.CharField(max_length=200)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    food_enegy_total = models.FloatField()
    food_enegy_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_enegy_name


class Foodingredient(models.Model):
    food_ingredient_name = models.CharField(max_length=200)
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    food_ingredient_ratio = models.FloatField()
    food_ingredient_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_ingredient_name

    def save(self, *args, **kwargs):
        self.food_ingredient_name = self.food_name.food_name + self.ingredient_name.ingredient_name
        return super().save(*args, **kwargs)


class Dailymeal(models.Model):
    dailymeal_name = models.CharField(max_length=200)
    dailymeal_rate = models.FloatField()
    dailymeal_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dailymeal_name


class Balancemeal(models.Model):
    balancemeal_name = models.CharField(max_length=200)
    dailymeal_name = models.ForeignKey(Dailymeal, on_delete=models.CASCADE)
    # name of ingredient
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # ratio of ingredient
    ingredient_ratio = models.FloatField()
    balancemeal_des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.balancemeal_name


class Dailyfamilyconsume(models.Model):
    family_name = models.CharField(max_length=200)
    dailymeal_name = models.ForeignKey(Dailymeal, on_delete=models.CASCADE)
    total_consume = models.IntegerField()
    cacbohydrate_consume = models.IntegerField()
    protein_consume = models.IntegerField()
    ion_consume = models.IntegerField()
    fat_consume = models.IntegerField()
    vitamin_consume = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.family_name


class Menusuggest(models.Model):

    menu_meal = models.ForeignKey(Balancemeal, on_delete=models.CASCADE)
    familysize = models.IntegerField()
    cacbohydrate_food_1 = models.ForeignKey(Foodingredient, on_delete=models.CASCADE)
    cacbohydrate_food_1_weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_meal


class MenuHistory(models.Model):

    menu_meal_history = models.ForeignKey(Balancemeal, on_delete=models.CASCADE)
    familysize = models.IntegerField()
    cacbohydrate_food_1 = models.IntegerField()
    cacbohydrate_food_1_name = models.CharField(max_length=100)
    cacbohydrate_food_1_weight = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_meal_history


class MenuActual(models.Model):

    menu_meal_actual = models.ForeignKey(Balancemeal, on_delete=models.CASCADE)
    familysize = models.IntegerField()
    cacbohydrate_food_1 = models.IntegerField()
    cacbohydrate_food_1_name = models.CharField(max_length=100)
    cacbohydrate_food_1_weight = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_meal_actual


class Information(models.Model):

    information_title = models.ForeignKey(Balancemeal, on_delete=models.CASCADE)
    information_content = models.TextField()
    information_image = models.CharField(max_length=200)
    information_ref = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_meal_actual


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content








