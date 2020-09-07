from django.urls import path,include
from . import views as users_view

urlpatterns = [
    path('register/',users_view.register,name='users-register'),
    path('',users_view.home,name='users-home'),
    path('destination/<int:id>/',users_view.destination,name='users-destination'),
    path('search/',users_view.search, name="search"),
    path('package/<int:package_id>/', users_view.detail_package, name='users-detail-package'),
    path('bookings/',users_view.bookings,name='users-bookings')

]