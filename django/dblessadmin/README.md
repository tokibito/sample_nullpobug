# dblessadmin

Djangoのsqlite3のDBが揮発性あっても使えるadmin

GAEなどで使えるかも

- signed cookieにセッションを保存
- LogEntryを作成する代わりにloggingでログを出力
    - GAEの場合はCloudLoggingを使うように設定を追加する必要あり
