from django.db import models

class WarikanModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    
    # タイトルを返す
    def __str__(self):
        return self.title

class MemberModel(models.Model):
    membername = models.CharField(max_length=100)

    # 名前を返す
    def __str__(self):
        return self.membername

class DetailModel(models.Model):
    memberID = models.ForeignKey(MemberModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    # タイトルを返す
    def __str__(self):
        return self.title