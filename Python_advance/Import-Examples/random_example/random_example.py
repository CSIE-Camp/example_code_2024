import random
import time

random.seed(time.time()) # 使用時間當作種子
print("random.random()\n  ", end="")
print(random.random()) # 顯示 0 到 1 之間的隨機數

print("random.randint(1, 10)\n  ", end="")
print(random.randint(1, 10)) # 顯示 1 到 10 之間的隨機整數

print("random.randrange(1, 10, 2)\n  ", end="")
print(random.randrange(1, 10, 2)) # 顯示 1 到 10 之間間格為 2 的隨機整數

print("random.choice([1, 2, 4, 8, 16])\n  ", end="")
print(random.choice([1, 2, 4, 8, 16])) # 隨機選擇一個元素

lis = [2, 4, 8, 16]
print("random.shuffle(lis)\n  ", end="") # 隨機排列
random.shuffle(lis)
print(lis)

