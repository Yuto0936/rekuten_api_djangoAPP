from django.db import models
from django.utils import timezone


class SearchWord(models.Model):
    class Meta:
        verbose_name = 'アーティスト名'
        verbose_name_plural = 'アーティスト名'
    
    word = models.CharField(max_length=255)
    flag = models.BooleanField(verbose_name='有効フラグ', default=False)
    def __str__(self):
        return self.word


class CD(models.Model):
    class Meta:
        verbose_name = 'cd情報'
        verbose_name_plural = 'cd情報'
    
    word = models.ForeignKey(SearchWord, on_delete=models.CASCADE, verbose_name='アーティスト名')
    jan = models.BigIntegerField('janコード', unique=True)
    salesDate = models.DateField('発売日', default=timezone.now, blank=True, null='True')
    title = models.CharField('cdタイトル', max_length=255)
    itemPrice = models.IntegerField('税込み価格', default=1, help_text='単位は円', blank=True, null=True)
    imageUrl = models.URLField('画像URL', blank=True, null=True)
    reviewAverage = models.FloatField('レビュー平均点', default=0, blank=True, null=True)
    reviewCount = models.IntegerField('レビュー件数', default=1, blank=True, null=True)
    itemUrl = models.URLField('商品URL', blank=True, null=True)
    def __str__(self):
        return self.title
