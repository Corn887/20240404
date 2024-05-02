import random

# 初始化累積獲勝次數
player_wins = 0
computer_wins = 0

# 建立個無限迴圈
while True:
    # 使用者輸入數字(出拳)
    player = int(input("請輸入 (0)剪刀 (1)石頭 (2)布 : "))
    if player == 0:
        print("使用者出了 剪刀")
    elif player == 1:
        print("使用者出了 石頭", player)
    elif player == 2:
        print("使用者出了 布", player)
    else:
        print("此為無效字元")

    # 電腦隨機出數字
    computer = random.randint(0, 2)
    if computer == 0:
        print("電腦出了 剪刀")
    elif computer == 1:
        print("電腦出了 石頭")
    elif computer == 2:
        print("電腦出了 布")

    # 判斷勝負
    if ((player == 0 and computer == 2) or
       (player == 1 and computer == 0) or
       (player == 2 and computer == 1)):
        print("恭喜，你贏了！")
        player_wins += 1
    elif player == computer:
        print("平手")
    else:
        print("抱歉，你輸了")
        computer_wins += 1

    # 顯示累積獲勝次數
    print("玩家累積獲勝次數:", player_wins)
    print("電腦累積獲勝次數:", computer_wins)
