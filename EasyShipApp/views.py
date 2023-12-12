from django.shortcuts import render

# Create your views here.
def paso_uno(request):
    return render(request, "EasyShipApp/paso_uno.html")
def paso_dos(request):
    return render(request, "EasyShipApp/paso_dos.html")
def paso_tres(request):
    return render(request, "EasyShipApp/paso_tres.html")