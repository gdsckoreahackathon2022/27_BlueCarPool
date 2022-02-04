from django.urls import path

from . import views

app_name = 'recruitment'

urlpatterns = [
    path('', views.recruit, name='recruit'),
    path('<int:recruit_id>/', views.detail, name='detail'),
    path('recruit/create/', views.recruit_create, name='recruit_create'),
    path('vote/recruit/<int:recruit_id>/', views.vote_recruit, name='vote_recruit'),
]