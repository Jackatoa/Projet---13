from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Event, Gallery
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import datetime

class HomeView(ListView):
    template_name = 'blog/accueil.html'
    context_object_name = 'posts'
    model = Post
    ordering = ['-date_posted']
    paginate_by = '3'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        now = datetime.datetime.now()
        events = Event.objects.filter(date__gte=now).order_by('date')[1:4]
        featuredevent = Event.objects.filter(date__gte=now).order_by('date')[:1]
        context.update({
            'events': events,
            'gallerys': Gallery.objects.all(),
            'featuredevents': featuredevent
        })
        return context

    def get_queryset(self):
        return Post.objects.order_by('-date_posted')

def home(request):
    context = {
        'posts': Post.objects.all(), 'events': Event.objects.all()
    }
    return render(request, 'blog/accueil.html', context, {'title': 'Accueil'})

def about(request):
    return HttpResponse('<h1>WESH ABOUT</h1>')

class EventListView(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'blog/saved_events.html'
    context_object_name = 'events'
    paginate_by = 9

    def get_queryset(self):
        return Event.objects.all()

class PostListView(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'blog/saved_posts.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        return Post.objects.all()

class GalleryListView(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'blog/saved_gallery.html'
    context_object_name = 'galleries'
    paginate_by = 9
        
    def get_queryset(self):
        return Gallery.objects.all()

@login_required
def gestion(request):
    return render(request, 'blog/gestion.html', {'title': 'Accueil'})