from .models import CD, SearchWord
import urllib.parse
import requests
from datetime import datetime


def get_word_list():
    """
    検索ワードリストの生成
    """
    word_list = []
    queryset = SearchWord.objects.all().filter(flag=True)
    for item in queryset:
        word_list.append(item.word)
    return word_list


def create_url(artistName):
    """
    検索ワードに登録されているワードのCD情報を検索
    """
    API = "https://app.rakuten.co.jp/services/api/BooksCD/Search/20170404"
    APPLICATION_ID = '1026633790552916121'
    values = {
        'applicationId': APPLICATION_ID,
        'format': 'json',
        'artistName': artistName,
    }
    # パラメータのエンコード処理
    params = urllib.parse.urlencode(values)
    # リクエスト用のURLを生成
    url = API + '?' + params
    return url


def lineNotify(message):
    """
    新発売のCDをlineに通知
    """
    line_notify_token = ''#ここにline公式サイトで作成したlineトークンを追加する
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)


def regist_data(data, artistName):
    """
    取得したデータをデータベースに登録
    """
    for i in range(len(data['Items'])):
        if not CD.objects.filter(jan=data['Items'][i]['Item']['jan']).exists():
            # 年月日を日付型に変換
            if '日' not in data['Items'][i]['Item']['salesDate']:
                salesDate = data['Items'][i]['Item']['salesDate'] + '01日'
                salesDate = salesDate.replace('年', '/').replace('月', '/').replace('日', '')
                salesDate = datetime.strptime(salesDate, '%Y/%m/%d')
            else:
                salesDate = data['Items'][i]['Item']['salesDate'].replace('年', '/').replace('月', '/').replace('日', '')
                salesDate = datetime.strptime(salesDate, '%Y/%m/%d')
            
            # 新規登録
            cd_data = CD.objects.create(
                word = SearchWord.objects.get(word=artistName),
                jan = data['Items'][i]['Item']['jan'],
                salesDate = salesDate,
                title = data['Items'][i]['Item']['title'],
                itemPrice = data['Items'][i]['Item']['itemPrice'],
                imageUrl = data['Items'][i]['Item']['mediumImageUrl'],
                reviewAverage = data['Items'][i]['Item']['reviewAverage'],
                reviewCount = data['Items'][i]['Item']['reviewCount'],
                itemUrl = data['Items'][i]['Item']['itemUrl'],
            )

            message = data['Items'][i]['Item']['itemUrl']
            lineNotify(message)

        # 既存エントリーの場合はレビュー数、レビュー平均値の差分だけを更新
        else:
            # 現在のCDレコードを取得
            cd_data = CD.objects.get(jan = data['Items'][i]['Item']['jan'])
            # 差分があれは更新
            if data['Items'][i]['Item']['reviewAverage'] != cd_data.reviewAverage:
                cd_data.reviewAverage = data['Items'][i]['Item']['reviewAverage']
            if data['Items'][i]['Item']['reviewCount'] != cd_data.reviewCount:
                cd_data.reviewCount = data['Items'][i]['Item']['reviewCount']
            # 反映
            cd_data.save()
