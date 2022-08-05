from django.db import models

class Comment(models.Model):
    pharmacyurl = models.TextField()
    pharmacyname = models.CharField(max_length=100)
    author = models.CharField(max_length=100) #Если бы автор был в Базе, можно было бы вписать ForeignKey()
    sources = models.TextField()
    date = models.CharField(max_length=100)
    text = models.TextField()
