from django.db import models
from django.contrib.auth.models import User
from users.models import UserBookings
# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    dtn_description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class DestinationImages(models.Model):

    ## Change it to Image Field afterwards
    image_name = models.CharField(max_length=200,default=None)
    small_image = models.ImageField(default="deault_small.jpeg",upload_to="destination_img")
    caraousel1 = models.ImageField(default="deault_big.jpeg",upload_to="destination_img")
    caraousel2 = models.ImageField(default="deault_big.jpeg",upload_to="destination_img")
    caraousel3 = models.ImageField(default="deault_big.jpeg",upload_to="destination_img")
    
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image_name}'

class Accomodation(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_description = models.TextField()
    price_per_room = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.hotel_name}'

class Travel(models.Model):
    
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price_per_person = models.PositiveIntegerField()

    ## For Travelling Choices
    TRAIN = 'TN'
    FLIGHT = 'FT'
    BUS = 'BS'

    TRAVELLING_CHOICES = [
        (TRAIN, 'Train'),
        (FLIGHT, 'Flight'),
        (BUS, 'Bus')
    ]

    travelling_mode = models.CharField(max_length=2,choices=TRAVELLING_CHOICES,default=FLIGHT)

    def __str__(self):
        return f'{self.departure} to {self.arrival} | {self.travelling_mode}'


class Package(models.Model):
    ## RelationShip Keys 
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    accomodation = models.ForeignKey(Accomodation,on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel,on_delete=models.CASCADE)
    bookings = models.ManyToManyField(User,through=UserBookings)

    ## Attributes
    package_name = models.CharField(max_length=200,default="NULL") # ye dalna
    adult_price = models.IntegerField()
    child_price = models.IntegerField() 
    description = models.TextField(default="NO DESCRIPTION ADDED")  
    inclusive = models.TextField()
    exclusive = models.TextField()
    number_of_days = models.PositiveIntegerField()
    number_of_times_booked = models.PositiveIntegerField(default=0)



    def __str__(self):
        return f'{self.package_name}'



class Itinerary(models.Model):
    package = models.OneToOneField(Package,on_delete=models.CASCADE,default=1)
    itinerary_name = models.CharField(max_length=200,default="NULL")

    def __str__(self):
        return f'{self.itinerary_name}'

class ItineraryDescription(models.Model):
    itinerary = models.ForeignKey(Itinerary,on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    itinerary_description = models.TextField()
    
    class Meta:
        ordering = ['day_number']

    
    def __str__(self):
        return f'{self.itinerary.itinerary_name} | Day {self.day_number}'