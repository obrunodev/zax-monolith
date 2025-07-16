from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from apps.accounts.models import Profile

# Define um inline admin para o Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfis'

# Redefine o UserAdmin para incluir o Profile
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-registra o UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Você também pode registrar o Profile separadamente se quiser
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
