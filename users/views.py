from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse



# Create your views here.
def paciente_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, '')

        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'doctores/login.html', {'forms': form})

def user_register(request):
    # if this is a POST request we'll process the form data
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the form data to the database
            user = form.save()
            # log the user in
            login(request, user)
            return HttpResponseRedirect('success')  # Redirect to a success page
    else:
        form = UserCreationForm()
    return render(request, 'doctores/register.html', {'form': form})