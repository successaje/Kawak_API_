import math
from django.utils.html import strip_tags


def count_words(html_string):

    word_string = strip_tags(html_string)
    count = len(word_string.split())
    return count

def average_user_rating():

    pass