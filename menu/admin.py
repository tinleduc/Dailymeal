from django.contrib import admin
from .models import *


# Register your models here.
#
# class MenuAdminSite(admin.AdminSite):
#
#     def get_app_list(self, request):
#         """
#         Return a sorted list of all the installed apps that have been
#         registered in this site.
#         """
#         ordering = {
#                 Unit: 1,
#                 Jobcategory: 2,
#                 "Job": 3,
#                 "Relation": 4,
#                 "Agecategory": 5,
#                 "Weightcategory": 6,
#                 "Bloodpressurecategory": 7,
#                 "Heartbeatcategory": 8,
#                 "Healthstatus": 9,
#                 "Region": 10,
#                 "Subregion": 11,
#                 "Countrycategory": 12,
#                 "Country": 13,
#                 "District": 14,
#                 "Ward": 15,
#                 "Street": 16,
#                 "Address": 17,
#                 "Memberinfo": 18,
#                 "Familyconsume": 19,
#                 "Objectconsume": 20,
#                 "Foodcategory": 21,
#                 "Foodingredient": 22,
#                 "Balancemeal": 23,
#                 "Dailymeal": 24,
#                 "Dailyfamilyconsume": 25,
#                 "Menusuggest": 26,
#                 "MenuHistory": 27,
#                 "MenuActual": 28
#             }
#         app_dict = self._build_app_dict(request)
#
#         # Sort the apps alphabetically.
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
#
#         # Sort the models alphabetically within each app.
#
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering[x['name']])
#
#         return app_list
#
#
# admin.site = MenuAdminSite()
#
#
admin.site.register(Unit)
admin.site.register(Jobcategory)
admin.site.register(Job)
admin.site.register(Relation)
admin.site.register(Agecategory)
admin.site.register(Weightcategory)
admin.site.register(Bloodpressurecategory)
admin.site.register(Heartbeatcategory)
admin.site.register(Healthstatus)
admin.site.register(Region)
admin.site.register(Subregion)
admin.site.register(Countrycategory)
admin.site.register(Country)
admin.site.register(District)
admin.site.register(Ward)
admin.site.register(Street)
admin.site.register(Address)
admin.site.register(Memberinfo)
admin.site.register(Familyconsume)
admin.site.register(Objectconsume)
admin.site.register(Food)
admin.site.register(Foodchoice)
admin.site.register(Foodcategory)
admin.site.register(Ingredientcategory)
admin.site.register(Ingredient)
admin.site.register(Ingredientcount)
admin.site.register(Foodingredient)
admin.site.register(Balancemeal)
admin.site.register(Dailymeal)
admin.site.register(Dailyfamilyconsume)
admin.site.register(Menusuggest)
admin.site.register(MenuHistory)
admin.site.register(MenuActual)
admin.site.register(Comment)



