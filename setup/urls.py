"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from setup import settings
from playlist.views import MusicaCreateView,MusicaDeleteView,MusicaDetailView,MusicaListView,MusicaUpdateView,PlaylistCreateView,PlaylistDetailView,PlaylistDeleteView,PlaylistListView,PlaylistUpdateView


urlpatterns = [
    path('', PlaylistListView.as_view(),name='playlist_list'),
    path('create/', PlaylistCreateView.as_view(),name='playlist_create'),
    path('<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'),
    path('<int:pk>/edit/', PlaylistUpdateView.as_view(), name='playlist_update'),
    path('<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist_delete'),
    
    path('musicas/', MusicaListView.as_view(), name='musica_list'),
    path('musicas/create/', MusicaCreateView.as_view(), name='musica_create'),
    path('musicas/<int:pk>/', MusicaDetailView.as_view(), name='musica_detail'),
    path('musicas/<int:pk>/edit/', MusicaUpdateView.as_view(), name='musica_update'),
    path('musicas/<int:pk>/delete/', MusicaDeleteView.as_view(), name='musica_delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
