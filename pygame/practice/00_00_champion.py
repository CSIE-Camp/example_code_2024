ROWS = 8
COLS = 8

def calculate_weight(board, row, col, player, step):
    weight = 0
    opponent = 'X' if player == 'O' else 'O'

    # 權重增加：占角
    if (row, col) in [(0, 0), (0, COLS - 1), (ROWS - 1, 0), (ROWS - 1, COLS - 1)]:
        weight += 100

    # 權重減少：C位

    # 權重減少：星位
    
    # 權重增加：邊界格子
    
    # 權重減少：禁區格子
    
    # 權重改變：模擬翻轉
    
    # ……

    return weight