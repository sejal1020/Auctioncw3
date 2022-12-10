from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User

from django.contrib.auth import get_user_model
User = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']