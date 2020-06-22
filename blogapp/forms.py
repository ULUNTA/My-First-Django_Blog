from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        #モデルはPostを使う。
        model = Post
        #フィールドはタイトルとテキスト
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
