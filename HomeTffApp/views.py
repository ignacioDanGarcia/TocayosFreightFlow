from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "HomeTffApp/home.html")

def product(request):
    return render(request, "HomeTffApp/product.html")

def company(request):
    return render(request, "HomeTffApp/company.html")

def get_started(request):
    return render(request, "HomeTffApp/get_started.html")

