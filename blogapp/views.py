from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required



#ブログの一覧を表示するメソッド
def post_list(request):
    #model.pyのPostからpublished_dateの順に並べる
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogapp/post_list.html', {'posts': posts})

#ブログの詳細を表示するメソッド
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/post_detail.html', {'post': post})

#新しいブログを投稿するメソッド
@login_required
def post_new(request):
    #新しい投稿があったら、セーブボタンを押して、post_detailに戻る。
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    #
    else:
        form = PostForm()
        #forms.pyからformを呼び出す
    return render(request, 'blogapp/post_edit.html', {'form':form})

#投稿したブログを編集する
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        #フォームを保存する
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #postを編集するためにただフォームを開く
        form = PostForm(instance=post)
    return render(request, 'blogapp/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    #草稿となる行だけ集める。そしてcreated_date順に並べる
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blogapp/post_draft_list.html', {'posts':posts})

#投稿
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #↓で投稿をdraftからlistに移す。
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #↓で投稿を削除できる。
    post.delete()
    return redirect('post_list')

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comennt.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

#コメントを受け付ける。
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    #CommentFormを編集するためにただフォームを開く
    return render(request, 'blogapp/add_comment_to_post.html', {'form': form})
