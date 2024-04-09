# django-cors-headers利用例

## 呼び出し側

```
cd cors/
python3.12 -m http.server 8001
```

http://127.0.0.1:8001/ にブラウザでアクセス

## 呼び出される側（Django）

```
cd myproject/
python manage.py runserver
```

http://127.0.0.1:8000/ で起動（API）
