from django.urls import path
from . import views

urlpatterns = [
    #viewsのpost_list関数を使いますよという意味。
    path('', views.post_list, name='post_list')
]