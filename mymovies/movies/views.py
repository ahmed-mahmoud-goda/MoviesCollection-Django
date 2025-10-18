from django.urls import reverse_lazy
from django.views.generic import RedirectView , ListView , DetailView, CreateView, UpdateView, DeleteView
from .models import Movie
# Create your views here.

class MyMovies(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies.html'
    ordering = ['name']
    
class MovieDetails(DetailView):
    model = Movie
    template_name ='movieDetail.html'
    pk_url_kwarg = 'movieId'

class MovieCreate(CreateView):
    model = Movie
    template_name= 'movieCreate.html'
    fields = ['name','released','category','description','image']
    success_url  = reverse_lazy('my-movies')

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name','category','released','description','image']
    template_name = 'movieUpdate.html'
    
    def get_object(self, queryset = ...):
        movie_id = self.kwargs.get('movieId')
        return Movie.objects.get(id = movie_id)

    def get_success_url(self):
        return reverse_lazy('movie-details',kwargs={'movieId':self.object.id})

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('my-movies')
    pk_url_kwarg = 'movieId'

class RedirectToMovies(RedirectView):
    pattern_name = 'my-movies'

    