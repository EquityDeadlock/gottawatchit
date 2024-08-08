from django.forms import ModelForm
from .models import Media, Tag


class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = '__all__'

class TagForm(ModelForm):
    class Meta:
        model = Tag 
        fields = '__all__'
