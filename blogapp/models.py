from django.conf import settings
from django.db import models
from django.utils import timezone

#以下このclass(object)とはなんぞやという説明。models.Modelの記述がデータベースに保存するべきものとわかるように。
class Post(models.Model):
    #AUTH_USER_MODELはログイン時のID。on_delete=models.CASCADEは例えばブログを削除したら、それに紐づくコメントも消える感じ。
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #ブランクもnullもTrueということは最初は入っていない？
    published_date = models.DateTimeField(blank=True, null=True)

    #publishはメソッドの名前。このメソッドを使って、pablish_dateの項目をつくるのか？
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#python manage.py makemigrations blogappとターミナルに入力し、データベースに追加するファイルを作る。
#python manage.py migrate blogappでデータベースにファイルを追加する。