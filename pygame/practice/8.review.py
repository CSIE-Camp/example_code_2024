import pygame
import sys

# 顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 寬度與長度
WIDTH = 600
HEIGHT = 800

# 遊戲初始化
pygame.init()

# 創建視窗
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 遊戲的標題
pygame.display.set_caption("My game")

# 遊戲迴圈
# 創建一個時鐘
clock = pygame.time.Clock()
while True:
    # 處理遊戲的幀數
    clock.tick(60)  
    # 取得使用者的所有輸入
    for event in pygame.event.get():
        # 當使用者按下關閉視窗，便退出遊戲
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 視窗顏色
    screen.fill(WHITE)

    # 綜合練習

    
    pygame.display.update()
