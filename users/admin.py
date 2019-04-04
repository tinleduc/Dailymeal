from django.contrib import admin
from .models import *

# Register your models here.
#
#
# class MenuAdminSite(admin.AdminSite):
#
#     def get_app_list(self, request):
#         """
#         Return a sorted list of all the installed apps that have been
#         registered in this site.
#         """
#         ordering = {
#             "User": 1,
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


# admin.site = MenuAdminSite()
#
admin.site.register(User)
