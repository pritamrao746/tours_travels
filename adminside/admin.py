from django.contrib import admin
from .models import (Accomodation,Destination,Travel,Itinerary,Package,
                     ImagesDestination,ItineraryDescription)

# Register your models here.
admin.site.register(Accomodation)
admin.site.register(Destination)
admin.site.register(Travel)
admin.site.register(Itinerary)
admin.site.register(Package)
admin.site.register(ImagesDestination)
admin.site.register(ItineraryDescription)