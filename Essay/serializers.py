from rest_framework import serializers

from .models import Essay

class EssaySerializer(serializers.ModelSerializer):

    class Meta:

        model = Essay
        
        fields = [
            'id',
            'EssayContent',
            'Created_at',
            'TokenCost',
            'Topic',
            'Title'
        ]