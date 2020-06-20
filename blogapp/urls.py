from django.urls import path
from . import views

urlpatterns = [
    #viewsのpost_list関数を使いますよという意味。
    path('', views.post_list, name='post_list'),
    #int型のpk（変数）がviews.pyに渡される。
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
]