from rest_framework import serializers
from .models import Event, Venue

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_name',
        read_only=True
    )

    # venue_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Venue.objects.all(),
    #     source='venue'
    # )
 
    class Meta:
        model = Event
        fields = ('__all__')
        # fields = ('event_name', 'venue_name', 'event_type', 'event_description', 'event_date', 'event_time', 'ticket_price', 'ticket_quantity' )



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
        fields = ('__all__')
        # fields = ( 'venue_name', 'address', 'description', 'venue_url', 'url', 'events')



