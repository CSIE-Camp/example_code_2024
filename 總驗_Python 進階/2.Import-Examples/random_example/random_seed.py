import random

print("random.seed()\n  ", end="")
random.seed()  # 跟 seed(time.time()) 一樣
print(random.random())
print("random.seed(1)\n  ", end="")
random.seed(1)  # set 1 as seed
print(random.random())
