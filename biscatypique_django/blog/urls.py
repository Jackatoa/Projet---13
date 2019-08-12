"""biscatypique_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import (EventListView, 
    PostListView, 
    GalleryListView, 
    HomeView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    GalleryDetailView, 
    GalleryCreateView, 
    GalleryUpdateView, 
    GalleryDeleteView,
    EventDetailView, 
    EventCreateView, 
    EventUpdateView, 
    EventDeleteView,
    )

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('accueil/', HomeView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('gestion/', views.gestion, name='blog-gestion'),
    path('saved_events/', EventListView.as_view(), name='blog-saved_events'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('saved_posts/', PostListView.as_view(), name='blog-saved_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('saved_gallery/', GalleryListView.as_view(), name='blog-saved_gallery'),
    path('gallery/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),
    path('gallery/new/', GalleryCreateView.as_view(), name='gallery-create'),
    path('gallery/<int:pk>/update/', GalleryUpdateView.as_view(), name='gallery-update'),
    path('gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='gallery-delete'),
    path('presentation/', views.presentation, name='blog-presentation'),
    path('staff/', views.staff, name='blog-staff'),
    path('contact/', views.contact, name='blog-contact'),
    path('tsa_day/', views.tsa_day, name='blog-tsa_day'),
]
