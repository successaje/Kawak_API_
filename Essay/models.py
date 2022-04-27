from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.db.models.signals import pre_save
from django.conf import settings

from accounts.models import User
from .utils import count_words

from markdown_deux import markdown

class EssayManager(models.Manager):

    def active(self, *args, **kwargs):
        return super(EssayManager, self).filter(draft=False).filter(publish_lte =timezone.now())

def upload_location(instance, filename):
    EssayModel = instance.__class__
    new_id = EssayModel.objects.order_by("id").last().id + 1

    return "%s/%s" %(new_id, filename)


class Essay(models.Model):

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
    title = models.TextField(max_length = 50, null=True)
    slug = models.SlugField(unique= True, null=True)
    Topic = models.CharField(choices = CATEGORY_OPTIONS, max_length=50)
    draft = models.BooleanField(default=False)
    EssayContent = models.TextField(null=True)
    Created_at = models.DateTimeField(auto_now=True, auto_now_add= False)
    read_time = models.IntegerField(default=0)
    No_of_Reviewers = models.IntegerField(default = 2)
    TokenCost = models.IntegerField()
    #UserRating = models.PositiveIntegerField(default= 0)
    #timestamp = models.DateTimeField( auto_now_add = True, default = 0)

    objects = EssayManager()

    class Meta:
        ordering = ["-Created_at"]

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.user)+" is created the **"+str(self.title)+"** Essay"

    def get_absolute_url(self):
        return reverse('essays:essay-detail', kwargs={"slug": self.slug})

    def get_api_url(self):
        return reverse('essays-api:essay-detail', kwargs={"slug": self.slug})

    def get_markdown(self):
        EssayContent = self.EssayContent
        markdown_text = markdown(EssayContent)
        return mark_safe(markdown_text)

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Essay.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_essay_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    if instance.EssayContent:
        html_string = instance.get_markdown()
        words_count = count_words(html_string)
        instance.count_words = words_count
        if instance.count_words < 100:
            return ("Minimum word count must be 100")

pre_save.connect(pre_save_essay_receiver, sender= Essay)

