# 猜數字遊戲
answer = 88
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while guess != answer and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = int(input("1~100的整數中猜個數字： ")) #用戶猜錯，回來迴圈
        if guess > answer:
            print("再小一點： ")
        elif guess < answer:
            print("再大一點： ")
    else:
        out_of_limit = True

if out_of_limit :
    print("你輸了")
else:
    print("恭喜你贏了")