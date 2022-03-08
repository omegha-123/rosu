from django.urls import path

from engapp import views

app_name='engapp'

urlpatterns=[
    path('index/',views.home),
    path('about/',views.about),
]
