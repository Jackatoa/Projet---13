from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Event, Gallery
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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

def event_presentation(request):
    return render(request, 'blog/event_presentation.html', {'title': 'Nos évènements'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/saved_posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post



@login_required
def gestion(request):
    return render(request, 'blog/gestion.html', {'title': 'Accueil'})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'link', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'link', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return True       
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        return True

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'content', 'link', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'content', 'link', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return True       
    
class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'
    
    def test_func(self):
        return True

class EventDetailView(DetailView):
    model = Event

class EventListView(ListView):
    model = Event
    template_name = 'blog/saved_events.html'
    context_object_name = 'events'
    paginate_by = 9
    
    def get_queryset(self):
        return Event.objects.all()    

class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = Gallery
    fields = ['title', 'content', 'link', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class GalleryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gallery
    fields = ['title', 'content', 'link', 'image']
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        return True       
        
class GalleryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gallery
    success_url = '/'
        
    def test_func(self):
        return True
    
class GalleryDetailView(DetailView):
    model = Gallery
    
class GalleryListView(ListView):
    model = Gallery
    template_name = 'blog/saved_gallery.html'
    context_object_name = 'gallerys'
    paginate_by = 9
    ordering = ['-date_posted']
            
    def get_queryset(self):
        return Gallery.objects.all()