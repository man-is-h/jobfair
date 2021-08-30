from django import forms
from django.contrib.auth.models import User
from jobfair_app.models import UserProfileInfo

class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password', )

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email-id','class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'})   
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('description', 'role', 'project')

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write about the project...', 'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),   
        }
