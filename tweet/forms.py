from django import forms 
from .models import Tweet, Comments
from django.contrib.auth.forms import UserCreationForm,ValidationError
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields =['text','image']
    def clean_text(self):
        text=self.cleaned_data.get('text')

        if len(text)<5:
            raise forms.ValidationError('Text must be at least 5 characters long')

        elif len(text)>100:
            raise forms.ValidationError('Text must be at most 100 characters long')

        return text

    def clean_image(self):
        image=self.cleaned_data.get('image')
        if image:
            if image.size > (1 * 1024 * 1024):
                raise forms.ValidationError('Image size must be less than 1MB')

            return image

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['text']
        
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=( 'username','email','password1','password2')