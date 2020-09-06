
from django.urls import path,include
from . import views as users_view

urlpatterns = [
    path('register/',users_view.register,name='users-register'),
    path('',users_view.home,name='users-home'),
    #path('package/',users_view.package,name='users-package'),
    path('destination/<int:id>/',users_view.destination,name='users-destination'),
    path('search/',users_view.search, name="search"),
    #path('package/<int:question_id>/', views., name='detail'),

]