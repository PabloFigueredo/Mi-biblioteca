
from django.urls import path
from .views import registro_web, login_web
from .views import logout_web
urlpatterns = [
    path('registro/', registro_web, name='registro'),
    path('login/', login_web, name='login'),
    path('logout/', logout_web, name='logout'),
]