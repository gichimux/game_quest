from rest_framework import serializers
from .models import Tournament

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('tournament_pic', 'name', 'details', 'owner','slots_available','date', 'cash_prize', 'ranking',  'ticket_prize')
