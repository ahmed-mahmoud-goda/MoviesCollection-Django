from django.urls import path
from .views import MyMovies , RedirectToMovies , MovieDetails,MovieCreate,MovieUpdate,MovieDelete

urlpatterns = [
    path('movies/',MyMovies.as_view(),name='my-movies'),
    path('movies/<int:movieId>/',MovieDetails.as_view(),name='movie-details'),
    path('movies/newmovie/',MovieCreate.as_view(),name='movie-create'),
    path('movies/<int:movieId>/edit/',MovieUpdate.as_view(),name='movie-edit'),
    path('movies/<int:movieId>/delete/',MovieDelete.as_view(),name='movie-delete'),
    path('',RedirectToMovies.as_view(),name='to-movies')
]
