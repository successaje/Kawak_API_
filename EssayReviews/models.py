from __future__ import unicode_literals
from audioop import reverse

from accounts.models import User

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class EssayReviewManager(models.Manager):
    def all(self):
        qs = super(EssayReviewManager, self).filter(parent = None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(EssayReviewManager, self).filter(content_type=content_type, object_id = obj_id).filter(parent=None)
        return qs

    def create_by_model_type(self, model_type, slug, EssayReviewContent, user, parent_obj=None):
        model_qs = ContentType.objects.filter(model = model_type)
        if model_qs.exists(): #or model_qs.count() != 1:
            SomeModel = model_qs.first().model_class()
            obj_qs = SomeModel.objects.filter(slug, self.slug)
            if obj_qs.exists() and obj_qs.count() == 1:
                instance = self.model()
                instance.EssayReviewContent = EssayReviewContent
                instance.user = user
                instance.content_type = model_qs.first()
                instance.object_id = obj_qs.first().id
                if parent_obj:
                    instance.parent= parent_obj
                instance.save()
                return instance
        return None
                


class EssayReview(models.Model):

    CATEGORY_OPTIONS = [
        ('Art', 'Art'),
        ('Anatomy', 'Anatomy'),
        ('Biology', 'Biology'),
        ('Blockchain', 'Blockchain'),
        ('Business', 'Business'),
        ('Comedy', 'Comedy'),
        ('Communication', 'Communication'),
        ('Design', 'Design'),
        ('Education', 'Education'),
        ('Engineering', 'Engineering'),
        ('Finance', 'Finance'),
        ('Health', 'Health'),
        ('History', 'History'),
        ('Games', 'Games'),
        ('Law', 'Law'),
        ('Linguistics', 'Linguistics'),
        ('Literature', 'Literature'),
        ('Politics', 'Politics'),
        ('Philosophy', 'Philosophy'),
        ('Religion', 'Religion'),
        ('Sciences', 'Sciences'),
        ('Others', 'Others'),
    ]

    user  = models.ForeignKey(to = User, on_delete=models.CASCADE)
    #Title = models.TextField(max_length = 50)
    object_id = models.PositiveIntegerField(default = 0)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,default=False, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')
    EssayReviewContent = models.TextField(null = True)
    submitted_at = models.DateTimeField(auto_now=True)
    #timestamp = models.DateTimeField(auto_now_add= True)

    #objects = 

    class Meta:

        ordering = ['-submitted_at']
        
    def __unicode__(self):
        return str(self.user.username)

    def __str__(self):
        return str(self.user)+" reviewed an Essay"

    def get_delete_url(self):
        return reverse("EssayReviews:delete", kwargs={'id': self.id})

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
