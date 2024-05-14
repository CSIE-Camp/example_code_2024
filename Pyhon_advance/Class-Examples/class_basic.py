# test 1
class test_1:
    x = 1
    def show():
        print("test_1")

print("test_1:")
print("  ", end="")
print(test_1) # 顯示 test_1 這個 class
##################################################
print("  test_1.show():")
print("    ", end="")

test_1.show() # 使用 test_1 這個 class 的 show()
##################################################
print("  test_1.x:")
print("    ", end="")

print(test_1.x) # 顯示 test_1 這個 class 的 a
print("##########################")


a = test_1 # 把 a 設定為 test_1 這個 class
# 動作同上
print("a:")
print("  a:\n    ", end="")
print(a)
print("  a.show():\n    ", end="")
a.show()
print("  a.x:\n    ", end="")
print(a.x)
##################################################
print("##########################")
a.x = 2 # 把 a 的 x 改成 2
print("a.x:\n    ", end="")
print(a.x)
b = test_1 # 把 b 設定為 test_1 這個 class
print("b.x:\n    ", end="")
print(b.x) # 顯示 b 的 x
