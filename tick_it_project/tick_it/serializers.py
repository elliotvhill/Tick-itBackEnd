from rest_framework import serializers
from .models import Event, Venue

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name = 'venue_detail'
        read_only = True
        many = True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset = Venue.objects.all(),
        source = 'venue'
    )

    class Meta:
        model = Venue
        fields = ( )



class VenueSerializer(serializers.HyperlinkedModelSerializer):



