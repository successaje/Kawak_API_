from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
)

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from .models import EssayReview

User = get_user_model()
def create_essaysreviews_serializer(model_type='post', slug =None, parent_id=None, user=None):
    class EssayReviewCreateSerializer(ModelSerializer):

        class Meta:
            model = EssayReview
            fields = [
                'id',
                #'object_id',
                #'content_type',
                #'content_object',
                #'parent',
                'EssayReviewContent',
                'submitted_at',
                #'Title'
            ]

        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            self.slug= slug
            self.parent_obj = None
            if parent_id:
                parent_qs = EssayReview.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count()==1:
                    self.parent_obj = parent_qs.first()
            return super(EssayReviewCreateSerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            model_type = self.model_type
            model_qs = ContentType.objects.filter(model = model_type)
            if not model_qs.exists() or model_qs.count() != 1:
                raise ValidationError("This is not a valid content type")

            SomeModel = model_qs.first().model_class()
            obj_qs = SomeModel.objects.filter(slug = self.slug)
            if  not obj_qs.exists() or obj_qs.count() != 1:
                raise ValidationError("This is not a slug for this content type")
            return data

        def create(self, validated_data):
            EssayReviewContent = validated_data.get("EssayReviewContent")
            if user:
                main_user = user
            else:
                main_user = User.objects.all().first()
            #user = User.objects.all().first()

            model_type = self.model_type
            slug = self.slug
            parent_obj = self.parent_obj
            essayreview = EssayReview.objects.create_by_model_type(
                model_type, slug, EssayReviewContent, main_user,
                parent_obj= parent_obj, 
            )
            return essayreview

    return EssayReviewCreateSerializer

class EssayReviewListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'EssayReviews-api:essays-reviews-details',
    )
    reviews_count = SerializerMethodField()
    class Meta:
        model = EssayReview
        fields = [
            'url',
            'id',
            #'object_id',
            #'content_type',
            #'content_object',
           # 'parent',
            'EssayReviewContent',
            'reviews_count',
            'submitted_at',
            #'Title'
        ]

    def get_reviews_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

class EssayReviewDetailSerializer(ModelSerializer):
    user = UserDetail
    reviews_count = SerializerMethodField()
    content_object_url = SerializerMethodField()
    reviews = SerializerMethodField()
    class Meta:
        model = EssayReview
        fields = [
            'id',
            #'object_id',
            #'content_type',
            #'content_object',
            #'parent',
            'EssayReviewContent',
            'reviews_count',
            'submitted_at',
            'content_object_url',
            #'Title'
        ]

        read_only_fields = [
            #'object_id',
            #'content_type',
            'reviews_count',
            'reviews',

        ]

    def get_content_object_url(self, obj):
        try:
            return obj.content_object.get_api_url()
        except:
            return None

    def get_reviews_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
