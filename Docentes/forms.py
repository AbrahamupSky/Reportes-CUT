from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full -ml-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'})) 
  codigoUDG = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'w-full -ml-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'}))
  nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'w-full -ml-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'}))
  apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'w-full -ml-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'}))

  class Meta:
    model = User
    fields = ['username', 'nombre', 'apellido', 'codigoUDG', 'email', 'password1', 'password2']

  def __init__(self, *args, **kwargs):
    super(UserCreationForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['class'] = 'w-full -ml-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'
    self.fields['password1'].widget.attrs['class'] = 'w-full -ml-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'
    self.fields['password2'].widget.attrs['class'] = 'w-full -ml-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'
