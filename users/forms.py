from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField()
    location = forms.CharField()
    student_class = forms.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone_number',
            'student_class',
            'location',
            'password1',
            'password2'
        ]