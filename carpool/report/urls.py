from unicodedata import name
from django.urls import path

from . import views

app_name='report'

urlpatterns=[
    path('' ,views.index,name='index'),
    path('<int:report_id>/',views.detail,name='detail'),
    path('answer/create/<int:report_id>/',views.answer_create,name='answer_create'),
    path('report/create/',views.report_create, name='report_create'),

]