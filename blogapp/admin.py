from django.contrib import admin
#models.pyで作ったclass(Post)を使う。
from .models import Post, Comment

#adminサイトにPost,Commentを追加する。
admin.site.register(Post)
admin.site.register(Comment)
