try:
    a = input()
    a = int(a)
except ValueError: # 如果有 ValueError
    print("Value error")
else: # 如果沒有錯誤
    print("No error")
finally: # 不管有沒有錯誤都會執行
    print("Finally")