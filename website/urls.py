from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index.urls'),
    path('contact/',views.contact,name='contact-url')
]

