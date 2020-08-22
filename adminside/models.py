from django.db import models

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
    image_name = models.CharField(max_length=100)
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
        return f'{self.arrival} to {self.departure}'

class Itinerary(models.Model):
    itinerary_name = models.CharField(max_length=200,default="NULL")
    day_number = models.PositiveIntegerField()
    itinerary_description = models.TextField()

    def __str__(self):
        return f'{self.itinerary_name} day{self.day_number}'

class Package(models.Model):
    ## RelationShip Keys 
    destination = models.OneToOneField(Destination,on_delete=models.CASCADE)
    accomodation = models.OneToOneField(Accomodation,on_delete=models.CASCADE)
    itinerary = models.OneToOneField(Itinerary,on_delete=models.CASCADE)
    travel = models.OneToOneField(Travel,on_delete=models.CASCADE)

    ## Attributes
    package_name = models.CharField(max_length=200,default="NULL")
    adult_price = models.IntegerField()
    child_price = models.IntegerField()
    inclusive = models.TextField()
    exclusive = models.TextField()
    number_of_days = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.package_name}'

