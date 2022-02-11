from django.urls import path

from api.views import movie_list_details
from .views import (
    index, category, movie, movie_details, movie_list, movie_list_details
)

urlpatterns = [
    path('movie/details/<int:movie_id>/',
         movie_details.get_movie_details, name="movie-details-id"),
    path('movie/details/', movie_details.get_movie_details, name="movie-details"),
    path('movie/<int:movie_id>/', movie.get_movie, name="movie-id"),
    path('movie/', movie.get_movie, name="movie"),
    path('movie-list/details/<int:list_id>/',
         movie_list_details.get_movie_list_details, name="movie-list-details-id"),
    path('movie-list/details/', movie_list_details.get_movie_list_details,
         name="movie-list-details"),
    path('movie-list/create/', movie_list.create_movie_list,
         name="create-movie-list"),
    path('movie-list/add-movie/<int:list_id>/',
         movie_list.add_movie_to_list, name="add-movie-id"),
    path('movie-list/add-movie/', movie_list.add_movie_to_list, name="add-movie"),
    path('movie-list/remove-movie/<int:list_id>/',
         movie_list.remove_movie_from_list, name="remove-movie-id"),
    path('movie-list/remove-movie/',
         movie_list.remove_movie_from_list, name="remove-movie"),
    path('movie-list/delete/<int:list_id>',
         movie_list.delete_movie_list, name="delete-movie-list-id"),
    path('movie-list/delete/', movie_list.delete_movie_list,
         name="delete-movie-list"),
    path('movie-list/<int:list_id>/',
         movie_list.get_movie_list, name="movie-list-id"),
    path('movie-list/', movie_list.get_movie_list, name="movie-list"),
    path('category/<int:category_id>/',
         category.get_category, name="category-id"),
    path('category/', category.get_category, name="category"),
    path('', index.index, name="index"),
]
