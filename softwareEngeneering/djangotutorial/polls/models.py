import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):  
        return self.choice_text



class Amount_Type(models.Model):
    name = models.CharField(max_length=100, primary_key= True)

class Item_Type(models.Model):
    unique_barcode = models.CharField(max_length=100, primary_key= True)
    name =models.CharField(max_length = 100)
    amount_type = models.ForeignKey(Amount_Type, on_delete=models.CASCADE)


class Individual_Items(models.Model):
    ID = models.CharField(max_length=100, primary_key= True)
    Expiration_date = models.DateTimeField(max_length=100)
    Type = models.ForeignKey(Item_Type, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Shopping_List(models.Model):
    Item_Type = models.ForeignKey(Item_Type, primary_key= True, on_delete=models.CASCADE)
    amount = models.IntegerField()
