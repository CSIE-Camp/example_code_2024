class Book:
    def __init__(self, lan, ti):  # 把兩個值輸進來
        self.language = lan  # 把第一個值設定給 language
        self.title = ti  # 把第二個值設定給 title
        self.ti_lan = ti + f" ({lan})"  # 把 title 和 language 組合起來

    # TODO Show all values

    # def __str__(self): # 在 print() Book 時會顯示 return 的值
    #     return f"test_3 {self.language} = {self.title} = {self.ti_lan}"

    def show_all(self):  # 顯示所有值
        print(f"test_3 {self.language} - {self.title} - {self.ti_lan}")  # 顯示所有值


A = Book("English", "How to learn Python")  # 把 English 和 How to learn Python 丟進去
print("A:")
print("  print(A):\n    ", end="")
A.show_all()

# TODO Show all values
# print(A) # 顯示 A


# FIXME 猜猜看下面的程式碼會印出什麼，A 到底會不會被 B 蓋掉

# B = Book("Chinese", "Python Programming") # 把 Chinese 和 Python Programming 丟進去
# print("B:")
# print("  print(B):\n    ", end="")
# print(B) # 顯示 B
# print("  print(A):\n    ", end="")
# print(A) # 顯示 A
