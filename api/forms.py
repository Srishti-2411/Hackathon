from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super( UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "first_name","last_name","password1", "password2", "email"]:
            self.fields[fieldname].help_text = None
            
    
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","password1", "password2", "email"]
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email"]