from .models import Patsient
from django.contrib.auth.forms import forms



class PatsientForms(forms.ModelForm):
    class Meta:
        model = Patsient
        fields = ['name', 'email', "city", "street", "password"]
        widget={
            'password' : forms.PasswordInput(),
        }

