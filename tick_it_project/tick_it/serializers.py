from rest_framework import serializers
from .models import Event, Venue

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_name',
        read_only=True
    )
 
    class Meta:
        model = Event
        fields = ('id', 'event_name', 'venue', 'event_type', 'event_description', 'event_date', 'event_time', 'ticket_price', 'ticket_quantity' )


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many=True,
        read_only=True
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue-detail'
    )

    class Meta:
        model = Venue
        fields = ('id', 'venue_name', 'address', 'description', 'venue_url', 'url', 'events')

