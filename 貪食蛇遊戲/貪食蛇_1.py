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

# 建立遊戲視窗
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('貪食蛇')

# 定義貪食蛇
def snake(block_size, snake_list):
    for x_y in snake_list:
        pygame.draw.rect(game_display, green, [x_y[0], x_y[1], block_size, block_size])

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

    # 遊戲迴圈
    while not game_exit:

        while game_over:
            game_display.fill(white)
            font = pygame.font.SysFont(None, 50)
            text = font.render('Game Over! Press C to play again or Q to quit', True, red)
            game_display.blit(text, (window_width / 4, window_height / 3))
            pygame.display.update()

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

        # 設定蛇移動的邊界

        if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
            game_over = True
        # 更新蛇的位置
        lead_x += lead_x_change
        lead_y += lead_y_change

        # 繪製遊戲畫面
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                game_over = True

        snake(block_size, snake_list)
        pygame.display.update()

        # 碰撞偵測
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, window_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, window_height - block_size) / block_size) * block_size
            snake_length += 1

        # 控制遊戲速度
        clock.tick(fps)

    pygame.quit()
    quit()

# 開始遊戲
game_loop()