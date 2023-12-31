from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('email', 'username')
