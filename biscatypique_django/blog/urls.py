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
    path('gallery/new/', GalleryCreateView.as_view(), name='gallery-create'),
    path('gallery/<int:pk>/update/', GalleryUpdateView.as_view(), name='gallery-update'),
    path('gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='gallery-delete'),
    path('presentation/', views.presentation, name='blog-presentation'),
    path('staff/', views.staff, name='blog-staff'),
    path('contact/', views.contact, name='blog-contact'),
    path('tsa_day/', views.tsa_day, name='blog-tsa_day'),
    path('project/', views.project, name='blog-project'),
    path('action/', views.action, name='blog-action'),
    path('partnaires/', views.partners, name='blog-partners'),
    path('mention/', views.mention, name='blog-mention'),
    path('tsa_descri/', views.tsa_descri, name='blog-tsa_descri'),
    path('tsa_state/', views.tsa_state, name='blog-tsa_state'),
    path('tsa_depis/', views.tsa_depis, name='blog-tsa_depis'),
    path('tsa_acco/', views.tsa_acco, name='blog-tsa_acco'),
    path('tsa_pris/', views.tsa_pris, name='blog-tsa_pris'),
    path('tsa_alte/', views.tsa_alte, name='blog-tsa_alte'),
    path('tsa_info/', views.tsa_info, name='blog-tsa_info'),
    path('tsa_ress/', views.tsa_ress, name='blog-tsa_ress'),
    
]
