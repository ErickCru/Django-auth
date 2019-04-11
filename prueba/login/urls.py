from django.urls import path
from .views import IndexView, LogOut


urlpatterns = [
    path('accounts/login/', IndexView.as_view(), name="login"),
    path("salir", LogOut, name="logout"),
]
