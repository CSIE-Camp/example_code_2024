import pygame
import sys
import random
from collections import deque
import copy
import math
import time


ROWS = 8
COLS = 8
WIDTH = 80
HEIGHT = 80
RADIUS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_PINK = (255, 182, 193)
LIGHT_BLUE = (173, 216, 230)
LINE_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
HINT_COLOR = (0, 255, 0)
TIMER_FONT_SIZE = 24


def ai_design(board, player, step):
    possible_moves = []
    for row in range(ROWS):  # 記錄所有合法位置
        for col in range(COLS):
            if is_valid_move(board, row, col, player):
                possible_moves.append((row, col))
    if player == 'O':
        max_weight = float('-inf')  # 初始化最大權重為負無窮大無窮大
        best_move = None  # 初始化最佳位置
        if possible_moves:  # 如果有合法位置
            for move in possible_moves:
                row, col = move  # (row, col)賦予合法位置
                board_copy = copy.deepcopy(board)  # 複製棋盤
                weight = calculate_weight_A(board_copy, row, col, player, step)  # 計算權重
                if weight > max_weight:  # 找出最佳位置
                    max_weight = weight
                    best_move = (row, col)
            # print('max: ', max_weight)
            return best_move
        else:
            return None
    else:
        max_weight = float('-inf')  # 初始化最大權重為負無窮大無窮大
        best_move = None  # 初始化最佳位置
        if possible_moves:  # 如果有合法位置
            for move in possible_moves:
                row, col = move  # (row, col)賦予合法位置
                board_copy = copy.deepcopy(board)  # 複製棋盤
                weight = calculate_weight_B(board_copy, row, col, player, step)  # 計算權重
                if weight > max_weight:  # 找出最佳位置
                    max_weight = weight
                    best_move = (row, col)
            # print('max: ', max_weight)
            return best_move
        else:
            return None


def calculate_weight(board, row, col, player, step):
    weight = 0
    opponent = 'X' if player == 'O' else 'O'

    # 權重增加：占角
    if (row, col) in [(0, 0), (0, COLS - 1), (ROWS - 1, 0), (ROWS - 1, COLS - 1)]:
        weight += 100

    # 權重減少：C位
    if (row, col) in [(0, 1), (1, 0), (6, 0), (7, 1), (7, 6), (6, 7), (1, 7), (0, 6)]:
        weight -= 10

    # 權重減少：星位
    if (row, col) in [(1, 1), (6, 1), (6, 6), (1, 6)]:
        weight -= 50
    
    # 權重增加：邊界格子
    
    # 權重減少：禁區格子
    
    # 權重改變：模擬翻轉
    
    # ……

    return weight


def initialize_board():
    board = [[' ' for i in range(COLS)] for i in range(ROWS)]
    board[3][3] = 'O'
    board[3][4] = 'X'
    board[4][3] = 'X'
    board[4][4] = 'O'
    return board


def draw_board(screen, board, player_turn, timer, surrender_button, skip_button, last_move):
    screen.fill(GREEN)
    font = pygame.font.Font(None, 36)

    # 顯示目前玩家
    player_color = 'Black' if player_turn == 'X' else 'White'
    turn_text = font.render(f"Player: {player_color}", True, TEXT_COLOR)
    screen.blit(turn_text, (10, HEIGHT * ROWS + 20))

    # 顯示棋子數量
    count_x, count_o = count_discs(board)
    count_text = font.render(f"Black: {count_x}  White: {count_o}", True, TEXT_COLOR)
    screen.blit(count_text, (10, HEIGHT * ROWS + 60))

    # 顯示倒數計時
    timer_text = font.render(f"Time Left: {timer:.1f} s", True, TEXT_COLOR)
    screen.blit(timer_text, (WIDTH * COLS - 200, HEIGHT * ROWS + 20))

    # 顯示投降按鈕
    pygame.draw.rect(screen, WHITE, surrender_button)
    surrender_text = font.render("Surrender", True, TEXT_COLOR)
    screen.blit(surrender_text, (WIDTH * COLS - 140, HEIGHT * ROWS + 60))

    # 顯示跳過按鈕
    pygame.draw.rect(screen, LIGHT_BLUE, skip_button)
    skip_text = font.render("Skip", True, TEXT_COLOR)
    screen.blit(skip_text, (WIDTH * COLS // 2 - 25, HEIGHT * ROWS + 60))

    # 紀錄合法的位置
    possible_moves = []
    for row in range(ROWS):
        for col in range(COLS):
            if is_valid_move(board, row, col, player_turn):
                possible_moves.append((row, col))

    # 顯示棋盤上的數字（列數、行數）
    for i in range(ROWS):
        number_text = font.render(str(i), True, TEXT_COLOR)
        screen.blit(number_text, (0, i * HEIGHT))
    for j in range(COLS):
        number_text = font.render(str(j), True, TEXT_COLOR)
        screen.blit(number_text, (j * WIDTH, 0))

    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, LINE_COLOR, (col * WIDTH, row * HEIGHT, WIDTH, HEIGHT), 2)  # (螢幕, 顏色, 矩形, 寬度（未填滿）)
            if board[row][col] == 'X':  # 黑棋
                pygame.draw.circle(screen, BLACK, (col * WIDTH + WIDTH // 2, row * HEIGHT + HEIGHT // 2), RADIUS)
            elif board[row][col] == 'O':  # 白棋
                pygame.draw.circle(screen, WHITE, (col * WIDTH + WIDTH // 2, row * HEIGHT + HEIGHT // 2), RADIUS)
            if (row, col) == last_move:  # 標示出上一步下的位置
                pygame.draw.rect(screen, HINT_COLOR, (col * WIDTH, row * HEIGHT, WIDTH, HEIGHT), 5)
            if (row, col) in possible_moves:  # 標示出合法的位置
                pygame.draw.circle(screen, HINT_COLOR, (col * WIDTH + WIDTH // 2, row * HEIGHT + HEIGHT // 2), RADIUS // 2)

    pygame.display.update()


def is_valid_position(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


def is_valid_move(board, row, col, player):
    if not is_valid_position(row, col) or board[row][col] != ' ':
        return False
    # 八方位
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]  
    opponent = 'X' if player == 'O' else 'O'  # 對手棋子

    for d_row, d_col in directions:  # 測試八方位
        r, c = row + d_row, col + d_col
        if is_valid_position(r, c) and board[r][c] == opponent:  # 至少一個對手的棋子
            r, c = r + d_row, c + d_col
            while is_valid_position(r, c) and board[r][c] == opponent:  # 直到不是對手的棋子
                r, c = r + d_row, c + d_col
            if is_valid_position(r, c) and board[r][c] == player:  # 如果是自己的棋子
                return True

    return False


def make_move(board, row, col, player):
    if is_valid_move(board, row, col, player):
        # 八方位
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]  
        opponent = 'X' if player == 'O' else 'O'

        board[row][col] = player  # 設定為自己的棋子

        side = 0  # 翻轉前邊界的棋子
        other = 0  # 翻轉前其他的棋子
        for r in range(0, 7):  # 計算翻轉前的棋子
            for c in range(0, 7):
                if board[r][c] == player:
                    if r == 0 or r == 7 or c == 0 or c == 7:
                        side += 1
                    else:
                        other += 1
        
        for d_row, d_col in directions:
            r, c = row + d_row, col + d_col
            if is_valid_position(r, c) and board[r][c] == opponent:
                flip_positions = []
                while is_valid_position(r, c) and board[r][c] == opponent:  # 直到不是對手的棋子
                    flip_positions.append((r, c))  # 紀錄可能翻轉的棋子
                    r, c = r + d_row, c + d_col
                if is_valid_position(r, c) and board[r][c] == player:  # 如果是自己的棋子
                    for flip_row, flip_col in flip_positions:  # 將紀錄的棋子全部翻轉
                        board[flip_row][flip_col] = player

        side_new = 0  # 翻轉後邊界的棋子
        other_new = 0  # 翻轉後其他的棋子
        for r in range(0, 7):  # 計算翻轉後的棋子
            for c in range(0, 7):
                if board[r][c] == player:
                    if r == 0 or r == 7 or c == 0 or c == 7:
                        side_new += 1
                    else:
                        other_new += 1

        flip_side = side_new - side  # 計算翻轉幾個邊界棋子
        flip_other = other_new - other  # 計算翻轉幾個其他棋子

        return flip_side, flip_other
    else:
        return None


def count_discs(board):
    count_x = sum(row.count('X') for row in board)
    count_o = sum(row.count('O') for row in board)
    return count_x, count_o


def display_winner(screen, winner, count_x, count_o):
    screen.fill(GREEN)  # 背景
    
    # Win!
    font = pygame.font.Font(None, 72)
    text = font.render(f"{winner} Win!", True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH * COLS // 2, HEIGHT * ROWS // 2 - 70))
    screen.blit(text, text_rect)
    
    # Black:
    # White:
    font_small = pygame.font.Font(None, 60)
    text_x = font_small.render(f"Black: {count_x}", True, TEXT_COLOR)
    text_o = font_small.render(f"White: {count_o}", True, TEXT_COLOR)
    text_x_rect = text_x.get_rect(midtop=(text_rect.centerx, text_rect.bottom + 50))
    text_o_rect = text_o.get_rect(midtop=(text_rect.centerx, text_x_rect.bottom + 10))
    screen.blit(text_x, text_x_rect)
    screen.blit(text_o, text_o_rect)
    
    # Click blank to continue
    # font_tip = pygame.font.Font(None, 48)
    # tip_text = font_tip.render("Click blank to continue", True, HINT_COLOR)
    # tip_rect = tip_text.get_rect(midtop=(text_rect.centerx, text_o_rect.bottom + 50))
    # screen.blit(tip_text, tip_rect)

    pygame.display.update()


def game_menu(screen):
    font = pygame.font.Font(None, 36)  # (字型, 大小)
    menu_text = font.render("Choose Game Mode:", True, TEXT_COLOR)  # (文字, 反鋸齒化, 顏色)
    screen.blit(menu_text, (WIDTH * COLS // 2 - 130, HEIGHT * ROWS // 2 - 50))  # (決定好的文字, (寬, 高))

    two_players_button = pygame.Rect(WIDTH * COLS // 2 - 120, HEIGHT * ROWS // 2, 230, 50)  # (左上座標x, 左上座標y, 寬, 高)
    player_computer_button = pygame.Rect(WIDTH * COLS // 2 - 120, HEIGHT * ROWS // 2 + 70, 230, 50)
    computer_computer_button = pygame.Rect(WIDTH * COLS // 2 - 120, HEIGHT * ROWS // 2 + 140, 230, 50)
    # (螢幕, 顏色, 決定好的矩形)
    pygame.draw.rect(screen, LIGHT_BLUE, two_players_button)  
    pygame.draw.rect(screen, LIGHT_BLUE, player_computer_button)
    pygame.draw.rect(screen, LIGHT_BLUE, computer_computer_button)
    # 創建三種文本（遊戲的模式）
    two_players_text = font.render("Player vs Player", True, TEXT_COLOR)
    player_computer_text = font.render("Player vs CPU", True, TEXT_COLOR)
    computer_computer_text = font.render("CPU vs CPU", True, TEXT_COLOR)

    screen.blit(two_players_text, (WIDTH * COLS // 2 - 100, HEIGHT * ROWS // 2 + 10))
    screen.blit(player_computer_text, (WIDTH * COLS // 2 - 90, HEIGHT * ROWS // 2 + 80))
    screen.blit(computer_computer_text, (WIDTH * COLS // 2 - 80, HEIGHT * ROWS // 2 + 150))

    pygame.display.update()  # 更新螢幕

    while True:
        for event in pygame.event.get():  # 檢索鍵盤、滑鼠等等
            if event.type == pygame.QUIT:  # 點擊視窗關閉
                pygame.quit()  # 清理 Pygame 的模組狀態，釋放資源
                sys.exit()  # 結束 Python 程式
            # 判斷玩家選擇的遊玩模式
            if event.type == pygame.MOUSEBUTTONDOWN:  # 按下了滑鼠按鈕
                mouseX, mouseY = pygame.mouse.get_pos()  # return (x座標, y座標)
                if two_players_button.collidepoint(mouseX, mouseY):  # collidepoint 檢查(x, y)是否在矩形內部
                    return 'two_players'
                elif player_computer_button.collidepoint(mouseX, mouseY):
                    return 'player_computer'
                elif computer_computer_button.collidepoint(mouseX, mouseY):
                    return 'computer_computer'


def battle_group_set():
    import shutil
    teamW = input("input teamW program name: ")
    teamB = input("input teamB program name: ")
    shutil.copy(teamW, "teamW.py")
    shutil.copy(teamB, "teamB.py")
    return

def main():
    # pygame 初始化
    pygame.init()
    # 創建螢幕
    screen = pygame.display.set_mode((WIDTH * COLS, HEIGHT * ROWS + 100))
    # 遊戲的標題
    pygame.display.set_caption('黑白棋')
    # 顯示遊戲選單
    game_mode = game_menu(screen)
    # 初始化棋盤
    board = initialize_board()
    
    player_turn = 'X'  # 初始化順序
    timer = 30  # 初始化計時器
    clock = pygame.time.Clock()  # pygame 時鐘物件
    
    # 投降按鈕
    surrender_button = pygame.Rect(WIDTH * COLS - 200, HEIGHT * ROWS + 50, 50, 40)
    # 跳過按鈕
    skip_button = pygame.Rect(WIDTH * COLS // 2 - 50, HEIGHT * ROWS + 50, 100, 40)
    winner = None  # 初始化贏家
    last_move = None  # 初始化上一步
    step = 0  # 初始化步數
    



    # 遊戲迴圈
    while True:
        # 繪製棋盤
        draw_board(screen, board, player_turn, timer, surrender_button, skip_button, last_move)
        for event in pygame.event.get():  # 檢索鍵盤、滑鼠等等
            if event.type == pygame.QUIT:  # 點擊視窗關閉
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # 按下了滑鼠按鈕
                mouseX, mouseY = pygame.mouse.get_pos()  # return (x座標, y座標)
                clicked_row = mouseY // HEIGHT  # HEIGHT => 每行高度
                clicked_col = mouseX // WIDTH  # WIDTH => 每列寬度
                if surrender_button.collidepoint(mouseX, mouseY):  # 點擊投降按鈕
                    if player_turn == 'X':
                        winner = 'O'
                    else:
                        winner = 'X'
                elif skip_button.collidepoint(mouseX, mouseY):  # 點擊Skip按鈕
                    player_turn = 'O' if player_turn == 'X' else 'X'
                    timer = 30
                # 下棋位置的合法性
                elif is_valid_move(board, clicked_row, clicked_col, player_turn):
                    step += 1
                    # 移動棋子
                    make_move(board, clicked_row, clicked_col, player_turn)
                    last_move = (clicked_row, clicked_col)  # 記錄下的位置
                    player_turn = 'O' if player_turn == 'X' else 'X'
                    timer = 30

        if (game_mode == 'player_computer' and player_turn == 'O') or game_mode == 'computer_computer':
            step += 1
            ai_move = ai_design(board, player_turn, step)
            if ai_move is None:
                player_turn = 'X' if player_turn == 'O' else 'O'
                timer = 30
            else:
                # 移動棋子
                make_move(board, ai_move[0], ai_move[1], player_turn)
                last_move = (ai_move[0], ai_move[1])
                player_turn = 'X' if player_turn == 'O' else 'O'
                timer = 30

        possible_moves_O = []  # 白棋合法的位置
        for row in range(ROWS):
            for col in range(COLS):
                if is_valid_move(board, row, col, 'O'):
                    possible_moves_O.append((row, col))

        possible_moves_X = []  # 黑棋合法的位置
        for row in range(ROWS):
            for col in range(COLS):
                if is_valid_move(board, row, col, 'X'):
                    possible_moves_X.append((row, col))
        # 處理勝負
        count_x, count_o = count_discs(board)
        if count_x + count_o == ROWS * COLS or winner or count_x == 0 or count_o == 0 or (not possible_moves_O and not possible_moves_X):  # 遊戲結束條件
            draw_board(screen, board, player_turn, timer, surrender_button, skip_button, last_move)
            pygame.time.wait(1000)
            if winner:  # 投降
                winner_color = 'Black' if winner == 'X' else 'White'
            elif count_x == 0:  # 黑棋0子
                winner_color = 'White'
            elif count_o == 0:  # 白棋0子
                winner_color = 'Black'
            else:  # 比棋數
                winner_color = 'Black' if count_x > count_o else 'White'
                if count_x == count_o:
                    winner_color = 'Tie'
            # 顯示贏家
            display_winner(screen, winner_color, count_x, count_o)
            waiting = True  # 初始化等待
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # 點擊視窗關閉按鈕
                        pygame.quit()
                        sys.exit()
            pygame.quit()
            sys.exit()

        dt = clock.tick(30) / 1000  # 幀率=30 返回兩次調用之間經過的毫秒
        timer -= dt
        if timer <= 0:
            player_turn = 'O' if player_turn == 'X' else 'X'
            timer = 30

battle_group_set()
from teamW import calculate_weight as calculate_weight_A
from teamB import calculate_weight as calculate_weight_B

if __name__ == "__main__":
    main()