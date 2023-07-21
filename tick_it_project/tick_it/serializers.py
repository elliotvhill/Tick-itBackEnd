from rest_framework import serializers
from .models import Event, Venue

class EventSerializer(serializers.HyperlinkedModelSerializer):
   
 
    class Meta:
        model = Event
        fields = ('event_name', 'venue_name', 'event_type', 'event_description', 'event_date', 'event_time', 'ticket_price', 'ticket_quantity' )



class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many = True,
        read_only = True
    )


    class Meta:
        model = Venue
        fields = ( 'venue_name', 'address', 'description', 'url', 'events')



