from django.urls import path


from HomeTffApp import views
app_name = 'HomeTffApp' 

urlpatterns = [
    path('', views.home, name="Home"),
    path('product/', views.product, name="Product"),
    path('company/', views.company, name="Company"),
    path('get_started/', views.get_started, name="Get started"),
]

"""
Home
Product
Company
Get Started    
"""