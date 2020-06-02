from django import forms
from .models import SearchWord


class SearchWordForm(forms.ModelForm):
    """
    新規データ登録画面のフォーム定義
    """
    class Meta:
        model = SearchWord
        fields = ['word', 'flag']