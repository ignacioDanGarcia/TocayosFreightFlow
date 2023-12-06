from django.urls import path


from HomeTffApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('product', views.home, name="Product"),
    path('company', views.home, name="Company"),
    path('get_started', views.home, name="Get started"),
]

"""
Home
Product
Company
Get Started    
"""