from django.urls import path
from .views import RegistroView, LoginView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='api_registro'),
    path('login/', LoginView.as_view(), name='api_login'),
]