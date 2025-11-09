from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class IMDBRating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, related_name="imdb_rating")
    rating = models.FloatField() 
   
    def __str__(self):
        return f"{self.movie.title} - {self.rating}"



class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.title} - {self.album.title}"



class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie, related_name="actors")

    def __str__(self):
        return self.name
