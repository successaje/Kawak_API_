from rest_framework import serializers
from .models import Contact_Us

class Contact_Us_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Contact_Us

        fields = ['name', 'email', 'message', 'date']

        def validate(self, attrs):
            name = attrs.get('email', '')
            email =  attrs.get('email', ' ')
            message = attrs.get('message','')

            return attrs