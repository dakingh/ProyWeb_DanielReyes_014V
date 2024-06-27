from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=1500000)
    codigo = forms.CharField(min_length=3, max_length=30)
    stock = forms.IntegerField(min_value=0, max_value=99)

    def clean_codigo(self):
        codigo = self.cleaned_data["codigo"]
        existe = Producto.objects.filter(codigo=codigo).exists()

        if existe:
            raise ValidationError("Este codigo ya existe!!!")
        return codigo

    class Meta:
        model = Producto
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]


class UserUpdateForm(UserChangeForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password_confirm = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password != password_confirm:
            self.add_error('password_confirm', "Las contraseñas no coinciden.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user