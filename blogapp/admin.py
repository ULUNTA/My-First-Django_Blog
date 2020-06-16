from django.contrib import admin
#models.pyで作ったclass(Post)を使う。
from .models import Post

#adminサイトにPostを追加する。
admin.site.register(Post)
