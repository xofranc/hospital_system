from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView




@login_required
class PacienteDashboardView(TemplateView):
    template_name = '/pacientes/paciente_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recetas'] = RecetaMedica.objects.filter(paciente=self.request.user)
        return context

# login de los doctroes
def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # Solo permitir login a usuarios marcados como "staff" (doctores)
            login(request, user)
            return redirect('doctor_dashboard')  # Redirigir a una página de dashboard
        else:
            messages.error(request, 'Credenciales inválidas o no eres un doctor autorizado.')
    return render(request, 'doctores/doctor_login.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctores/doctor_dashboard.html')

def pacientes_login(request):
    return redirect('pacientes:login')