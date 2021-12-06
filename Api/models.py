from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Movie(models.Model):
   title = models.CharField(max_length = 32)
   description = models.CharField(max_length = 360)
   
   def no_of_ratings(self):
       ratings= Rating.objects.filter(movie=self)
       return len(ratings)

   def avg_rating(self):
       ratings= Rating.objects.filter(movie=self)
       sum = 0
       for rating in ratings:
           sum+= rating.stars

       if len(ratings)>0:
           return sum/len(ratings)
       else:
           return 0

   def __str__(self):
       return self.title

class Rating(models.Model):
   movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   stars = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
   def __str__(self):
       return str(self.stars)

   class Meta:
       unique_together = [['user', 'movie'],]
       index_together = [["user", "movie"],]