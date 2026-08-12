

from django.urls import path
from .import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('<int:tweet_id>/comments/', views.comments_view, name='comments_view'),
    path('<int:tweet_id>/make_comment/', views.make_comment, name='make_comment')
] 
