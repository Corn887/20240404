import pygame
import random

# 初始化pygame
pygame.init()

# 設定遊戲視窗的寬和高
window_width = 800
window_height = 600

# 設定顏色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 設定每個方塊的大小
block_size = 20

# 設定遊戲速度
clock = pygame.time.Clock()
fps = 15

# 設定字型和字體大小
font = pygame.font.SysFont(None, 50)

# 建立遊戲視窗
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('貪食蛇')

# 定義貪食蛇
def snake(block_size, snake_list):
    for i, x_y in enumerate(snake_list):
        if i == 0:
            pygame.draw.rect(game_display, green, [x_y[0], x_y[1], block_size, block_size])
        else:
            pygame.draw.rect(game_display, black, [x_y[0], x_y[1], block_size, block_size])

# 顯示分數
def show_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    game_display.blit(score_text, (window_width - 150, 10))

# 顯示遊戲結束訊息
def game_over_message(score):
    game_display.fill(white)
    game_over_text = font.render('Game Over', True, red)
    score_text = font.render('Score: ' + str(score), True, black)
    game_display.blit(game_over_text, (window_width / 3, window_height / 3))
    game_display.blit(score_text, (window_width / 3, window_height / 2))
    pygame.display.update()

# 遊戲主迴圈
def game_loop():
    game_exit = False
    game_over = False

    # 蛇的起始位置和長度
    lead_x = window_width / 2
    lead_y = window_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snake_list = []
    snake_length = 1

    # 隨機產生食物的位置
    food_x = round(random.randrange(0, window_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, window_height - block_size) / block_size) * block_size

    # 記分板
    score = 0

    # 上一個按鍵事件
    last_key_event = None

    # 遊戲迴圈
    while not game_exit:

        while game_over:
            game_over_message(score)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                # 限制蛇在一次按鍵操作中只能轉90度
                if (event.key == pygame.K_LEFT and last_key_event != pygame.K_RIGHT) or \
                   (event.key == pygame.K_RIGHT and last_key_event != pygame.K_LEFT) or \
                   (event.key == pygame.K_UP and last_key_event != pygame.K_DOWN) or \
                   (event.key == pygame.K_DOWN and last_key_event != pygame.K_UP):
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_UP:
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = block_size
                        lead_x_change = 0
                    last_key_event = event.key

        # 更新蛇的位置
        lead_x += lead_x_change
        lead_y += lead_y_change

        # 處理蛇穿過邊界的情況
        if lead_x >= window_width:
            lead_x
        if lead_x >= window_width:
            lead_x = 0
        elif lead_x < 0:
            lead_x = window_width - block_size
        elif lead_y >= window_height:
            lead_y = 0
        elif lead_y < 0:
            lead_y = window_height - block_size

        # 檢查蛇是否碰到自己的身體
        snake_head = [lead_x, lead_y]
        if snake_head in snake_list[1:]:
            game_over = True

        # 繪製遊戲畫面
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [food_x, food_y, block_size, block_size])

        snake_list.insert(0, [lead_x, lead_y])
        if len(snake_list) > snake_length:
            del snake_list[-1]

        snake(block_size, snake_list)
        show_score(score)
        pygame.display.update()

        # 碰撞偵測
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, window_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, window_height - block_size) / block_size) * block_size
            snake_length += 1
            score += 1

        # 控制遊戲速度
        clock.tick(fps)

    pygame.quit()
    quit()

# 開始遊戲
game_loop()