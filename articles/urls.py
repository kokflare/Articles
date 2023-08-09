from django.urls import path
from .views import (
    ArticleListView,
    Articledetail,
    Articleupdate,
    Articledelete,
    Articlecreate)


urlpatterns=[
    path('<int:pk>/edit/', Articleupdate.as_view(), name='edit'),
    path('<int:pk>/', Articledetail.as_view(), name='detail'),
    path('<int:pk>/delete/', Articledelete.as_view(), name='delete'),
    path('new/', Articlecreate.as_view(), name='create'),
    path('', ArticleListView.as_view(), name='article_list')
]