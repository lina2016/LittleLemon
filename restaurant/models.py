from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    no_of_guests = models.SmallIntegerField(default=2,)

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField() 
    image = models.CharField(max_length=100, default='')
    menu_item_description = models.TextField(max_length=1000, default='',blank=True)
    
    def __str__(self):
        return f"{self.title} [ Price : {self.price}] [ Stock :{self.inventory}]"