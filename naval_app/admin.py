from django.contrib import admin
from naval_app.models import *

# Register your models here.

@admin.register(Buque)
class buqueadmin (admin.ModelAdmin):
    list_display = ("nombre", "imo", "eslora", "manga", "puntal", "tripulantes")
    list_display_links = ("nombre", "imo")
    search_fields =  ("nombre", "imo")
    ordering =  ("nombre", "imo")

#admin.site.register(Buque)



