from django.urls import path
from naval_app.views import index
from naval_app.views import crear_buque
from naval_app.views import listar_buques
urlpatterns = [
    path("", index , name="index"),
    path('buque/nuevo/', crear_buque, name="buque_form"),
    path('buques/', listar_buques, name='buque_list'),
    

]