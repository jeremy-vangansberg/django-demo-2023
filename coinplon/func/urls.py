from django.urls import path 
from . import views

urlpatterns = [
    path('func_list/', views.FunctionnalityListView.as_view(), name='func_list'),
    path('func_detail/<int:pk>', views.FunctionnalityDetailView.as_view(), name="func-detail"),
    path('func_create/', views.FunctionnalityCreateView.as_view(), name="func-create")
]
