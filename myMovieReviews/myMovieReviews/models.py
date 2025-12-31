from django.db import models

# Create your models here.

class Review(models.Model) :
    GENRE_CHOICES = [
        ('action', '액션'),
        ('romance', '로맨스'),
        ('comedy', '코미디'),
        ('drama', '드라마'),
        ('fantasy', '판타지'),
        ('horror', '공포'),
    ]
    title = models.CharField(max_length=30)
    poster = models.TextField()
    year = models.CharField(max_length=5)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    rate = models.FloatField()
    RT = models.IntegerField()
    content = models.TextField()
    Dir = models.CharField(20)
    MC = models.CharField(50)