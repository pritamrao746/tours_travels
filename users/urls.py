
from django.urls import path,include
from . import views as users_view

urlpatterns = [
    path('register/',users_view.register,name='users-register'),
    path('',users_view)
]