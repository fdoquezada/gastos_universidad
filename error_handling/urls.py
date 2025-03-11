from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_404, name='custom_404'),
    path('error/', views.custom_500, name='custom_500'),
]




handler404 = 'error_handling.views.custom_404'
handler500 = 'error_handling.views.custom_500'
