from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User
from .models import Chat,Message

@login_required
def chat_room(request, username):


    render(request, 'chat/chatroom.html')

