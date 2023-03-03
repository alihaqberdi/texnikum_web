from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import models
from .form import PatsientForm


# Create your views here.

def register_patsient_view(request):

    if request.method == 'POST':
        patsientForm = PatsientForm(request.POST)
        if patsientForm.is_valid():
            user = patsientForm.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('user:login')
    patsientForm = PatsientForm(request.POST)
    form = {'form': patsientForm}
    return render(request, 'registration/signup.html', {'form': form})


