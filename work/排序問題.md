泡沫排序法

> bubbleSort.py

```python
def sort(a):
    for i in range(len(a)):
        for j in range(i):
            if (a[j] > a[i]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    return a

print('sort([3, 8, 2, 1, 5]=', sort([3,8,2,1,5]))    
```



逐步改良法完成排序問題，可能會時間不穩定，但它是一個很活的方法，不像是泡沫排序，很死，基本上不會用

> randomImproveSort.py

```python
import random

def sort(a):
    n = len(a)
    for _ in range(0,n*n*10):
        i=random.randint(0, n-2)
        if (a[i] > a[i+1]):  # 檢查有沒有違規，違規就交換
            a[i], a[i+1] = a[i+1], a[i]
    return a

print('sort([3, 8, 2, 1, 5]=', sort([3,8,2,1,5]))
```

