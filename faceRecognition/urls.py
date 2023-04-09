from django.urls import path

from faceRecognition.views.views import top


urlpatterns = [
    path('', top, name='top'),
    path('result/', top, name='result'),
]
