from django.urls import path
from . import views

urlpatterns = [
    path('destination/', views.destination,name = 'destination'),
    path('accomodation/',views.accomodation,name = 'accomodation'),
    path('travel/',views.travel,name = 'travel'),
    path('itinerary/',views.itinerary,name = 'itinerary')

]