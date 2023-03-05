from django.urls import path
from .views import chat_room

app_name = 'user'


urlpatterns = [
    path('open/chat/', chat_room, name='chat_room'),
    # path('chat/<int:recipient_id>/', chat_room, name='chat_room'),
]
