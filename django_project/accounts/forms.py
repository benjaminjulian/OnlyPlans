from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

# Profile Form
class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Notandanafn', max_length=150)
    first_name = forms.CharField(label='Eiginnafn', max_length=255, required=False)
    last_name = forms.CharField(label='Eftirnafn', max_length=255, required=False)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            ]

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Notandanafn',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(label="Lykilorð", widget=forms.PasswordInput, required=True)

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Notandanafn', min_length=5, max_length=150)
    password1 = forms.CharField(label='Lykilorð', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Lykilorð (endurtekið)', widget=forms.PasswordInput)

    def clean_username(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("Notandanafn frátekið :'(")  
        return username  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Lykilorðin stemma ekki!")
        if password1 < "        ":
            raise ValidationError("Það vantar fleiri stafi í lykilorðið -- minnst átta!")
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user