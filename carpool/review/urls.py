from django.urls import path, include
from .import views

app_name = 'review'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:review_id>/', views.detail, name='detail'),
    path('review/create/', views.review_create, name='review_create'),
]