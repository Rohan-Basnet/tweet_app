from django.shortcuts import render
from .models import Tweet, Profile
from django.contrib.auth.models import User
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets= Tweet.objects.all().order_by('-created_at')

    query= request.GET.get('q', "")
    if query:
        tweets= tweets.filter(user__username__icontains=query)
    return render(request,'tweet_list.html',{'tweets':tweets, 'query':query})

@login_required
def tweet_create(request):
    if(request.method=='POST'):
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet= form.save(commit=False)
            tweet.user = request.user
            tweet.save()  
            return redirect('tweet_list' )
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method== 'POST':
        form= TweetForm(request.POST, request.FILES,instance=tweet)
        if form.is_valid:
            tweet= form.save(commit=False)
            tweet_user= request.user
            tweet.save()
            return redirect('tweet_list')
    else: 
        form= TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_delete(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})


def register(request):
    if(request.method=='POST'):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            text=form.cleaned_data['password1']
            user.set_password(text)
            user.save()
            login(request, user)
            return redirect('tweet_list')
        
    else:
        form= UserRegistrationForm()

    return render(request,'registration/register.html',{'form':form})

def profile_view(request, username):
    user=get_object_or_404( User, username=username)
    profile=get_object_or_404(Profile,user=user)
    tweet_count=Tweet.objects.filter(user=user).count()
    return render(request,'profile_view.html',{'user':user, 'profile':profile,'bio':profile.bio,'tweet_count':tweet_count})