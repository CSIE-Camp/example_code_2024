import math

print("pi:\n  ", end="")
print(math.pi) # 顯示 π

print("sqrt(4):\n  ", end="")
print(math.sqrt(4)) # 顯示根號 4

print("sin(pi / 2):\n  ", end="")
print(math.sin(math.pi / 2)) # 顯示 sin(π/2) = sin(90°) = 1

print("acos(0):\n  ", end="")
print(math.acos(0)) # 顯示 acos(0) = 90° = π/2

print("log(e):\n  ", end="")
# log 這裡預設是以 e 為底，也就是自然對數 ln
print(math.log(math.e)) # 顯示 ln(e) = 1 

print("log(100,10):\n  ", end="")
print(math.log(100, 10)) # 顯示 log10(100) = 2

print("log10(10):\n  ", end="")
print(math.log10(10)) # 也可以直接使用 log10

print("log2(16):\n  ", end="")
print(math.log2(16)) # 顯示 log2(16) = 4

print("180 degree = ? radian:\n  ", end="")
print(math.radians(180)) # 顯示 180° = π radian

print("pi radian = ? degree:\n  ", end="")
print(math.degrees(math.pi)) # 顯示 π radian = 180°
