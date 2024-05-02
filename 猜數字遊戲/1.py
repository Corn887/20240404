# 猜數字遊戲
answer = 88
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while guess != answer and not out_of_limit:
    guess_count += 1
    if guess_count < guess_limit:
        guess = int(input("1~100的整數中猜個數字： "))
        if guess > answer:
            print("再小一點： ")
        elif guess < answer:
            print("再大一點： ")   # 這個迴圈本來就預設是沒猜對時觸發，所以不需考慮等於的情況
    else:
        if guess_count == guess_limit:   # 猜到第3次當下還能再猜一次
            guess = int(input("1~100的整數中猜個數字： "))
            if guess > answer:   # 以下6列用於「若玩家在第3次猜對，也顯示為獲勝」
                out_of_limit = True
            elif guess < answer:
                out_of_limit = True
            else:
                out_of_limit = False

if out_of_limit :
    print("你輸了,答案是" + str(answer))
else:
    print("恭喜你贏了")