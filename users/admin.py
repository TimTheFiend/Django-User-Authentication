from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """ `list_display` allows us to customise what we want to
     List on the form. In this case we're overriding it to show
     age.
     """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'age', ]
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
