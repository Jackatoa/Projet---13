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
from .views import EventListView, PostListView, GalleryListView, HomeView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('accueil/', HomeView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('gestion/', views.gestion, name='blog-gestion'),
    path('saved_events/', EventListView.as_view(), name='blog-saved_events'),
    path('saved_posts/', PostListView.as_view(), name='blog-saved_posts'),
    path('saved_gallery/', GalleryListView.as_view(), name='blog-saved_gallery'),
]
