from django.urls import path, include
from guides import views


urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('activities/', views.activities, name='activities'),
    path('about-us/', views.about_us, name='about-us'),
    path('destinations/minsk/', views.minsk, name='minsk'),
    path('destinations/grodno/', views.grodno, name='grodno'),
    path('destinations/brest/', views.brest, name='brest'),
]
