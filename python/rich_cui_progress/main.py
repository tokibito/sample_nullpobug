import time
from rich.progress import track

values = list(range(10))
result = 0

for value in track(values, description="処理中..."):
    result += value
    time.sleep(0.5)  # 意図的に遅延させる

print(result)
