```python
def sort_colors(num: List<int>) -> List<int>:
    while True:
        idx = 0
        if idx < len(num)-2, num[idx] > num[idx+1]:
            tmp = num[idx]
            num[idx] = num[idx+1]
            num[idx+1] = tmp
            idx = idx+1



```
