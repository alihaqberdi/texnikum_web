from django.shortcuts import render
from user.models import User


# Create your views here.

def IndexView(request):
    user = User.objects.all()
    print(user)
    return render(request, 'index.html', {'user': user})


def ContactView(request):
    return render(request, 'contact.html')


def ElementsView(request):
    return render(request, 'elements.html')


def AboutView(request):
    return render(request, 'about.html')


def NewsView(request):
    return render(request, 'news.html')


def ServiceView(request):
    return render(request, 'services.html')
