from django import forms 
from .models import Tweet


class TweetForm(forms.Form):
    class Meta:
        model = Tweet
        fields =['text','image']
        
    
