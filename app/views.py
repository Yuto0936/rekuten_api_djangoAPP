from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.models import CD, SearchWord
from .forms import SearchWordForm
from django.urls import reverse_lazy
import subprocess


class CDListView(ListView):
    model = CD
    template_name = 'app/jan_list.html'
    def queryset(self):
        return CD.objects.all()


class SearchWordCreateView(CreateView):
    model = SearchWord
    form_class = SearchWordForm
    success_url = reverse_lazy('app:create_done')


def create_done(request):
    # 登録処理が正常終了した場合に呼ばれるテンプレート
    return render(request, 'app/create_done.html')


class WordListView(ListView):
    model = SearchWord
    template_name = 'app/searchword_list.html'
    def queryset(self):
        return SearchWord.objects.all()


class WordUpdateView(UpdateView):
    model = SearchWord
    form_class = SearchWordForm
    success_url = reverse_lazy('app:update_done')


def update_done(request):
    return render(request, 'app/update_done.html')


class WordDeleteView(DeleteView):
    model = SearchWord
    success_url = reverse_lazy('app:delete_done')


def delete_done(request):
    return render(request, 'app/delete_done.html')


def update_jan_info(request):
    """変数の初期化"""
    message = []
    rc_code = None
    if request.POST:
        cmd = 'python manage.py get_jan_info'
        rc_code = subprocess.call(cmd, shell=True)
        if rc_code == 0:
            message = "楽天CD情報の更新処理が正常終了しました。"
        else:
            message = "楽天CD情報の更新処理が異常終了しました。"
    return render(request, 'app/result.html', {'message': message,})