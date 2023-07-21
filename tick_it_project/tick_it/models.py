from django.db import models

# Create your models here.

class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.venue_name

class Event(models.Model):
    event_name =  models.CharField(max_length=100)
    venue_name = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=100)
    event_description = models.TextField(max_length=500)
    event_date = models.DateField()
    event_time = models.TimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.event_name
