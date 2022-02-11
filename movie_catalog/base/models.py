from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(null=False, unique=True)
    movie_name = models.CharField(max_length=200, null=False, unique=True)

    class Meta:
        db_table = 'movie'


class Category(models.Model):
    category_name = models.CharField(max_length=200, null=False, unique=True)

    class Meta:
        db_table = 'category'


class MovieCategoryMapping(models.Model):
    movie = models.ForeignKey(
        Movie, null=False, on_delete=models.CASCADE, to_field="movie_id")
    category = models.ForeignKey(
        Category, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie_category_mapping'
        unique_together = ('category_id', 'movie_id')


class MovieList(models.Model):
    list_name = models.CharField(max_length=200, null=False, unique=True)

    class Meta:
        db_table = 'movie_list'


class ListMovieMapping(models.Model):
    list = models.ForeignKey(MovieList, null=False, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, null=False, on_delete=models.CASCADE, to_field="movie_id")

    class Meta:
        db_table = 'list_movie_mapping'
        unique_together = ('list_id', 'movie_id')
