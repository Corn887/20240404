# 檔案讀取、寫入 3:10:22
    # open("檔案路徑", mode="開啟模式")
    # mode="r" 讀取
    # mode="r" 複寫
    # mode="r" 在原先的資料後寫東西
file = open("f1拷貝.py", mode="r")
print(file.read())  # 全部讀取
# print(file.readline())   # 只讀一列(下面再打一次就是只讀2列，跟上面那個擇一放)
file.close()

    # 讓它一列一列分開讀(方法1)
file = open("f2拷貝.py", mode="r")
for line in file:
    print(line)
file.close()

    # 讓它一列一列分開讀(方法2)
file = open("f3拷貝.py", mode="r")
print(file.readlines())
file.close()

    # 複寫成：
# file = open("f4拷貝.py", mode="w")
# file.write("hi")
# file.close()
    # 在原先的資料後寫東西
# file = open("f5拷貝.py", mode="a")
# file.write("\n你好")
# file.close()
    # 在原先的資料後寫東西(避免加上去的中文變成亂碼)
# file = open("f5拷貝.py", mode="a", encoding="utf-8")
# file.write("\n你好")
# file.close()
    # 省去每次都要close的麻煩
# with open("f5拷貝.py", mode="a", encoding="utf-8") as file:
#     file.write("\n哈哈")