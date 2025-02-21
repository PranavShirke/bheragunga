from django.urls import path
from Bindaas import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('speech-to-text/', views.speech_to_text, name='speech_to_text'),
    path('gesture-recognition/', views.gesture_recognition, name='gesture_recognition'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('video-tutorials/', views.video_tutorials, name='video_tutorials'),
    path('gestures/', views.gestures, name='gestures'),
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),
]

