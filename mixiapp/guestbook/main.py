# coding: utf-8
from datetime import timedelta
from google.appengine.ext import db
import webapp2
import json

PER_PAGE = 20


class Greeting(db.Model):
    user_id = db.StringProperty(u'ユーザーID')
    body = db.TextProperty(u'本文')
    ctime = db.DateTimeProperty(auto_now_add=True)

    @property
    def ctime_jst(self):
        """UTC+9の時刻を返す
        """
        if self.ctime:
            return self.ctime + timedelta(hours=9)

    def ctime_display(self):
        """時刻の文字列表現を返す
        """
        if self.ctime:
            return self.ctime_jst.strftime("%Y/%m/%d %H:%M:%S")


def get_greetings(offset=0):
    """Greetingを取得して返す
    """
    query = Greeting.all().order('-ctime')
    return query.fetch(PER_PAGE, offset)


def create_greeting(user_id, body):
    """Greetingを作成
    """
    return Greeting(user_id=user_id, body=body)


class GuestbookAPIHandler(webapp2.RequestHandler):
    def get(self):
        # オフセットパラメータを取得
        raw_offset = self.request.get('offset')
        try:
            offset = int(raw_offset)
        except ValueError:
            offset = 0
        # Greetingを取得
        greetings = get_greetings(offset)
        # 辞書に変換
        datas = []
        for greeting in greetings:
            datas.append({
                'user_id': greeting.user_id,
                'body': greeting.body,
                'ctime': greeting.ctime_display()})
        result = {
            'greetings': datas,
        }
        # JSONフォーマットで出力
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(result))

    def post(self):
        user_id = self.request.get('user_id')
        body = self.request.get('body')
        # Greetingを保存
        greeting = create_greeting(user_id, body)
        greeting.put()
        # JSONフォーマットで出力
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps({'status': 'OK'}))


application = webapp2.WSGIApplication([
    ('^/api/guestbook$', GuestbookAPIHandler),
])
