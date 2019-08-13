from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
import os

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['sujet']
            message = 'L\'email vient de {}... Le message est {} .. Email est {}'.format(cd['nom'], cd['message'], cd['email'])
            Email = '{}'.format(cd['email'])
            try:
                send_mail(subject, message , Email, [os.environ.get("EMAIL_USER")])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, f'Votre message a bien été envoyé !')
            return redirect('blog-home')
    return render(request, "blog/contact.html", {'form': form}, {'title': 'Nous contacter'})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')

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
        gallerys = Gallery.objects.all().order_by('date')[:3]
        context.update({
            'events': events,
            'gallerys': gallerys,
            'featuredevents': featuredevent,
            'title' : 'Accueil'
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
def project(request):
    return render(request, 'blog/projet.html', {'title': 'Nos projets'})

def action(request):
    return render(request, 'blog/action.html', {'title': 'Nos actions'})

def partners(request):
    return render(request, 'blog/partenaires.html', {'title': 'Nos partenaires'})



def tsa_day(request):
    return render(request, 'blog/tsa_day.html', {'title': 'Journée de sensibilisation à l\'autisme'})

def staff(request):
    return render(request, 'blog/staff.html', {'title': 'Les bénévoles'})

def presentation(request):
    return render(request, 'blog/presentation.html', {'title': 'Présentation'})

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
    fields = ['title', 'content', 'previewtext', 'link', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','previewtext', 'link', 'image']
    
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
    fields = ['title', 'content', 'price', 'starthour', 'endhour', 'adress', 'date', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'content', 'price', 'starthour', 'endhour', 'adress', 'date', 'image']
    
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
    fields = ['title', 'image', 'date', 'location', 'occasion', 'link']
 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class GalleryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gallery
    fields = ['title', 'image', 'date', 'location', 'occasion', 'link']
        
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
    
    
class GalleryListView(ListView):
    model = Gallery
    template_name = 'blog/saved_gallery.html'
    context_object_name = 'gallerys'
    paginate_by = 9
    ordering = ['-date_posted']
            
    def get_queryset(self):
        return Gallery.objects.all()

