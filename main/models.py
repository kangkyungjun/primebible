from django.db import models

# Create your models here.

class Bible(models.Model):
    class Meta:
        db_table = 'bible'
    sort = models.CharField(max_length=70, default='')
    book = models.CharField(max_length=70, default='')
    jang = models.CharField(max_length=70, default='')
    ki = models.TextField(max_length=256, default='')

class Bible_jang(models.Model):
    class Meta:
        db_table = 'bible_jang'
    sort = models.CharField(max_length=70, default='')
    book = models.CharField(max_length=70, default='')
    jang = models.CharField(max_length=70, default='')
    ki = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name

class BibleEng(models.Model):
    class Meta:
        db_table = 'bibleeng'
    sorteng = models.CharField(max_length=70, default='')
    booengk = models.CharField(max_length=70, default='')
    jangeng = models.CharField(max_length=70, default='')
    kieng = models.TextField(max_length=256, default='')