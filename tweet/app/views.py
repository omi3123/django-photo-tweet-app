from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TweetModel
from .forms import UserRegistrationForm
from .forms import TweetCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
def index(request):
    return HttpResponse('HEllo')

def list_tweet(request):
    tweets=TweetModel.objects.all()
    return render(request,'app/list_tweet.html',{
        'tweets' : tweets
    })
@login_required
def add_tweet(request):
    if request.method == 'POST':
        form=TweetCreateForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('list_tweet')
    else:
        form=TweetCreateForm()
    return render(request,'app/add_tweet.html',{
        'form' : form
    })

@login_required
def edit_tweet(request, tweet_id):
    tweet = TweetModel.objects.get(pk=tweet_id)  
    if request.method == 'POST':
        form = TweetCreateForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('list_tweet')
    else:
        form = TweetCreateForm(instance=tweet)  
    return render(request, 'app/edit_tweet.html', {'form': form})


from django.shortcuts import get_object_or_404, redirect
from .models import TweetModel
@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(TweetModel, pk=tweet_id)  
    if request.method == 'POST':
        tweet.delete() 
        return redirect('list_tweet')  
    return render(request, 'app/delete_tweet.html', {'tweet': tweet})  

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html', {'form': form})