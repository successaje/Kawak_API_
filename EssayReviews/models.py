from django.db import models
from accounts.models import User

class EssayReview(models.Model):

    CATEGORY_OPTIONS = [
        ('Art', 'Art'),
        ('Anatomy', 'Anatomy'),
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
    
    Reviewer  = models.ForeignKey(to = User, on_delete=models.CASCADE)
    Title = models.TextField(max_length = 50)
    Topic = models.CharField(choices = CATEGORY_OPTIONS, max_length=255)
    EssayReviewContent = models.TextField(default=False)
    submitted_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-submitted_at']

    def __str__(self):
        return str(self.Reviewer)+" reviewed an Essay"