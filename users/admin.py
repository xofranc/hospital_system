from django.contrib import admin
from .models import Usuarios

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'lastName', 'user_type', 'is_staff', 'is_active')
    search_fields = ('email', 'name', 'lastName')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active')
    ordering = ('email',)
    readonly_fields = ('date_joined',)  # Agrega 'date_joined' como campo de solo lectura

    # Campos que se mostrarán al editar un usuario
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'lastName', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),  # Muestra 'date_joined' como solo lectura
    )

    # Campos que se mostrarán al crear un usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'lastName', 'password1', 'password2'),
        }),
    )
    # Métodos para separar los usuarios en el panel de administración
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusuarios ven todos los usuarios
        return qs.filter(user_type='paciente')  # Otros usuarios solo ven pacientes

    def pacientes(self, request):
        return self.get_queryset(request).filter(user_type='paciente')

    def doctores(self, request):
        return self.get_queryset(request).filter(user_type='doctor')

    def superusuarios(self, request):
        return self.get_queryset(request).filter(is_superuser=True)

    # Registrar las vistas personalizadas
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('pacientes/', self.admin_site.admin_view(self.pacientes), name='pacientes'),
            path('doctores/', self.admin_site.admin_view(self.doctores), name='doctores'),
            path('superusuarios/', self.admin_site.admin_view(self.superusuarios), name='superusuarios'),
        ]
        return custom_urls + urls
    
    
    def get_list_display_links(self, request, list_display):
        return ['email']

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_links'] = [
            {'name': 'Pacientes', 'url': 'pacientes/'},
            {'name': 'Doctores', 'url': 'doctores/'},
            {'name': 'Superusuarios', 'url': 'superusuarios/'},
        ]
        return super().changelist_view(request, extra_context=extra_context)

# Registra el modelo de usuario personalizado con la clase CustomUserAdmin
admin.site.register(Usuarios, CustomUserAdmin)