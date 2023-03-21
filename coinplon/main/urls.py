from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('special/', views.special_view, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
]
