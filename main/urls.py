from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # NEW PAGES
    path('ultrasound/', views.ultrasound, name='ultrasound'),
    path('xray/', views.xray, name='xray'),
]