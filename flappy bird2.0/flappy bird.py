import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 遊戲視窗大小
WIDTH, HEIGHT = 600, 400
# 色彩設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 載入圖片並縮放
bird_img = pygame.image.load('img/bird.png')
bird_img = pygame.transform.scale(bird_img, (30, 30))  # 縮放鳥的圖片
pipe_img = pygame.image.load('img/pipe.png')
background_img = pygame.image.load('img/background.png')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # 縮放背景圖片

# 載入音效
score_sound = pygame.mixer.Sound('sounds/score.mp3')

# 載入背景音樂
pygame.mixer.music.load('sounds/background_music.mp3')
pygame.mixer.music.play(-1)  # 循環播放背景音樂

# 設定遊戲參數
gravity = 0.35  # 增加重力加速度
bird_movement = 0
score = 0
pipe_gap = 150  # 水管間距
pipe_speed = 3  # 水管移動速度

# 遊戲物件位置
bird_rect = bird_img.get_rect(center=(50, HEIGHT // 2))

# 初始化水管列表
pipes = []

# 建立遊戲視窗
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# 設定字體
font = pygame.font.SysFont(None, 40)

# 遊戲迴圈
running = True
game_over = False
while running:
    # 檢查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 4  # 增加向上的速度

    if not game_over:
        # 鳥的運動
        bird_movement += gravity
        bird_rect.centery += bird_movement

        # 背景和水管的運動
        for pipe in pipes:
            pipe[0] -= pipe_speed  # 管道向左移動

        # 更新水管位置
        if len(pipes) == 0 or pipes[-1][0] <= WIDTH - 200:  # 如果水管列表為空或上一個水管的 x 座標離左邊邊界還有 200 像素，則新增一組水管
            pipe_height = random.randint(50, HEIGHT - pipe_gap - 50)  # 隨機生成新水管的高度
            pipes.append([WIDTH, pipe_height])
            pipes.append([WIDTH, pipe_height - pipe_gap - pipe_img.get_height()])  # 添加對應的上水管

        # 檢查碰撞
        for pipe in pipes:
            pipe_rect = pygame.Rect(pipe[0], pipe[1], pipe_img.get_width(), pipe_img.get_height())
            if bird_rect.colliderect(pipe_rect) or bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
                game_over = True
                break

        # 檢查是否通過水管
        if len(pipes) >= 2 and pipes[0][0] + pipe_img.get_width() < bird_rect.left:
            score += 1
            score_sound.play()
            pipes.pop(0)  # 刪除通過的水管對
            pipes.pop(0)  # 刪除對應的上水管

    # 更新遊戲畫面
    win.blit(background_img, (0, 0))
    win.blit(bird_img, bird_rect)
    for pipe in pipes:
        win.blit(pipe_img, (pipe[0], pipe[1]))

    # 顯示分數
    score_text = font.render(f'Score: {score}', True, WHITE)
    win.blit(score_text, (10, 10))

    # 顯示遊戲結束畫面
    if game_over:
        game_over_text = font.render("Game Over", True, WHITE)
        win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

    pygame.display.update()
    pygame.time.Clock().tick(60)

# 退出遊戲
pygame.quit()
sys.exit()