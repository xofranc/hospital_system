from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages


from logins.forms import PatientRegistrationForm

app_name = 'pacientes'

class PacienteDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'pacientes/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info_medica'] = self.request.user.paciente_profile.info_medica
        return context

    def test_func(self):
        return not self.request.user.is_staff  # Solo pacientes, no doctores


def paciente_login(request):
    if request.method == 'GET':
        return render(request, 'pacientes/login.html', {
            'form': AuthenticationForm()
        })
    else:
        # Autenticar al usuario
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # Si la autenticación falla, mostrar un mensaje de error
            return render(request, 'pacientes/login.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            # Si la autenticación es exitosa, loguear al usuario y redirigir
            login(request, user)
            return redirect('pacientes:dashboard')

def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            # Guardar el usuario
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Encriptar la contraseña
            user.save()
            messages.success(request, 'Tu cuenta ha sido creada. Puedes iniciar sesión ahora.')
            return redirect('paciente_login')  # Redirigir a la página de login después del registro
    else:
        form = PatientRegistrationForm()
    return render(request, 'pacientes/register.html', {'form': form})  # Renderizar la plantilla de registro


@login_required
def out(request):
    logout(request)
    return redirect('home')
