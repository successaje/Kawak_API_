from rest_framework import serializers

from .models import WaitingList

class WaitingList(serializers.ModelSerializer):

    class Meta:

        model = WaitingList

        fields = [
            'name', 
            'email',
        ]


    def validate(self ,attrs):
        email = attrs.get('email', '',)
        name = attrs.get('name', '',)

        return attrs