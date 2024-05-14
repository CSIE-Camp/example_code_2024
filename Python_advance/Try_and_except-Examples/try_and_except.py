try:
    inp = input("Enter a number: ")
    if(inp=="1"):
        print(a) # 尚未宣告 a
    elif(inp=="2"):
        lis = [1, 2, 3]
        print(lis[3]) # 超出範圍
    elif(inp=="3"):
        int("a") # a 不是數字
    elif(inp=="4"):
        print(1 + "1") # 不能把 int 和 str 相加
    elif(inp=="5"):
        print(1 / 0) # 不能除以 0

# FIXME 猜猜看下面的程式抓得到什麼錯誤
    # elif(inp=="6"):
    #     print("test)

except NameError:
    print("NameError")
except IndexError:
    print("IndexError")
except ImportError:
    print("ImportError")
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except SyntaxError:
    print("SyntaxError")
except Exception:
    print("Other Error")