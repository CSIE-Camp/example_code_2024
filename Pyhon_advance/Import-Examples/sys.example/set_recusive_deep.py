import sys
sys.setrecursionlimit(10) # 設定最大遞迴深度（預設為 1000）
# 能執行的遞迴次數要減 4 
def rec(n):
    print(n)
    rec(n + 1)

rec(0)