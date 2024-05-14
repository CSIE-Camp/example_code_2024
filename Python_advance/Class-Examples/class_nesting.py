class nest:
    def __init__(self, input_1, input_2):
        self.inp_1 = input_1
        self.inp_2 = input_2
        self.inp_3 = input_1 + input_2
    class t1: # class 裡面也可以有 class
        def __init__(self, x, y): # 裡面也可以有自己的 __init__
            self.a = x
            self.b = y
            self.c = x + y
        def show(self): 
            print("123")
            print(self.a)
    class t2: # class 裡面也可以有多個 class
        def __init__(self):
            self.z = 1
    
N = nest(1, 2)
print("N:")
print("  print(N.inp_1):\n    ", end="")
print(N.inp_1) # 顯示 N 的 inp_1
print("  print(N.t1(1,2).c):\n    ", end="")
print(N.t1(1,2).c) # 顯示 N 的 t1 的 c
print("  N.t1(1,2).show():")
N.t1(1,2).show() # 執行 N 的 t1 的 show()
print("  print(N.t2().z):\n    ", end="")
print(N.t2().z) # 顯示 N 的 t2 的 z