# prompts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_prompt, name='submit_prompt'),
    path('upvote/<int:prompt_id>/', views.upvote_prompt, name='upvote_prompt'),
    path('search/', views.search_prompts, name='search_prompts'), # Add this line
]
