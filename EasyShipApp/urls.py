
from django.urls import path


from EasyShipApp import views
app_name = 'EasyShipApp' 

urlpatterns = [
    path('paso_uno/', views.paso_uno, name="Paso uno"),
    path('paso_dos/', views.paso_dos, name="Paso dos"),
    path('paso_tres/', views.paso_tres, name="Paso tres"),
]