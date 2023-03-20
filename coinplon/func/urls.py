from django.urls import path 
from . import views

urlpatterns = [
    path('func_list/', views.FunctionnalityListView.as_view(), name='func_list')
]
