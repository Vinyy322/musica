from django import forms
from .models import Playlist, Musica

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'

        