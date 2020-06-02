from app.utils import get_word_list, create_url, lineNotify, regist_data
from django.core.management.base import BaseCommand
from app.models import CD, SearchWord
from datetime import datetime
import requests
import urllib.request
import urllib.parse
import json
import logging


# 初期パラメータ設定
logdir = r'C:\Users\yuto_\OneDrive\Desktop\rakuten_api\cd\log'
date_name = datetime.now().strftime('%Y%m%d-%H%M%S')
file_name = logdir + "\\" + date_name + "_" + "GET_JAN_INFO.log"
logging.basicConfig(filename=file_name, level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class Command(BaseCommand):

    """カスタムコマンド定義"""

    def handle(self, *args, **options):
        print('Djangoカスタムコマンドのテストです')

        logging.info('start')
        # 検索ワードの取得
        word_list = get_word_list()
        # 検索ワードを1つずつ取り出してループ処理
        for artistName in word_list:
            # リクエスト用のURLを生成
            url = create_url(artistName)
            # リクエストを投げる
            req = requests.get(url)
            # json形式で取得
            data = json.loads(req.text)
            # データの登録 or 変更(新規ならLINEへ通知)
            regist_data(data, artistName)
        
        logging.info('finish')