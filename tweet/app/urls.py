from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('list_tweet/',views.list_tweet,name='list_tweet'),
    path('add_tweet/',views.add_tweet,name='add_tweet'),
    path('<int:tweet_id>/edit_tweet/',views.edit_tweet,name='edit_tweet'),
    path('<int:tweet_id>/delete_tweet/',views.delete_tweet,name='delete_tweet'),
    path('register/',views.register,name='register'),
]