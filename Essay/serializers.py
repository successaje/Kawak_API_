from rest_framework import serializers

from EssayReviews.serializers import EssayReviewListSerializer
from EssayReviews.models import EssayReview


from .models import Essay

class EssayCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Essay

        fields = [
            #'id',
            'title',
            'user',
            #'slug',
            'Topic',
            'EssayContent',
            'Created_at',
            'No_of_Reviewers',
            'TokenCost',
            #'UserRating',

        ]

class EssayListSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name=':essay-detail',
        lookup_field = 'id'
    )
    user = serializers.SerializerMethodField()
    class Meta:

        model = Essay
        
        fields = [
            'id',
            'url',
            'user',
            'title',
            'slug',
            'Topic',
            'EssayContent',
            'Created_at',
            "No_of_Reviewers",
            'TokenCost',
]
 
    def get_user(self, obj):
        return str(obj.user.username)

class EssayDetailSerializer(serializers.ModelSerializer):

    essayreviews = serializers.SerializerMethodField()

    class Meta:

        model = Essay

        fields = [
            'id',
            'user',
            'title',
            'slug',
            'Topic',
            'EssayContent',
            'Created_at',
            'TokenCost',
            'No_of_Reviewers',
            #'UserRating',
            'essayreviews',

        ]
    def get_essayreviews(self, obj):
        # content_type = obj.get_content_type
        # object_id = obj.id
        r_qs = EssayReview.objects.filter_by_instance(obj)
        essayreviews = EssayReviewListSerializer(r_qs, many = True).data
        return essayreviews

