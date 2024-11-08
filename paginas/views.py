from django.shortcuts import render

# Create your views here.
def dashboard_paciente(request):
    return render(request, 'paciente/dashboard.html')

def dashboard_doctor(request):
    return render(request, 'doctor/dashboard.html')

def home(request):
    return render(request, 'home.html')
