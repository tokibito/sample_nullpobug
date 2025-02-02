import time
from rich.progress import track

values = list(range(10))  # 0～9 の数値のリストを用意
result = 0

for value in track(values, description="処理中..."):
    result += value  # 値を足し合わせ
    time.sleep(0.5)  # 意図的に遅延させる

print(result)  # 結果表示
