from rest_framework import serializers

from .models import EssayReview

class EssayReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = EssayReview
        fields = [
            'id',
            'EssayReviewContent',
            'submitted_at',
            'Topic',
            'Title'
        ]