from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BarbijosFormulario(forms.Form):

    marca= forms.CharField(max_length=40)
    tamanio= forms.CharField(max_length=40)
    precio = forms.IntegerField(required=True)
    




class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
   
    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
     
    
    #class Meta:
     #   model = User
     #   fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        #Saca los mensajes de ayuda
      #  help_texts = {k:"" for k in fields


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label= "Ingrese su mail:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
   
    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        
     