
from django.urls import path
from .views import index, detail, NewList, NewDetail

urlpatterns = [
    path('news_list/', index, name='index'),
    path('new/<str:slug>', detail, name='detail'),
    path('', NewList.as_view()),
    path('int:pk',NewDetail.as_view()),
]