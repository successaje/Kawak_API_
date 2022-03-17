from django.db import models
from accounts.models import User

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
    Author  = models.ForeignKey(to = User, on_delete=models.CASCADE)
    Title = models.TextField(max_length = 512)
    Topic = models.CharField(choices = CATEGORY_OPTIONS, max_length=255)
    EssayContent = models.TextField(default=False)
    Created_at = models.DateTimeField(auto_now=True)
    TokenCost = models.IntegerField()

    class Meta:
        ordering = ["-Created_at"]

    def __str__(self):
        return str(self.Author)+" is created the **"+str(self.Title)+"** Essay"


