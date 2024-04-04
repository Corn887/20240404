#字串
print("吃飽沒")
# 數字
168.58
#布林值
True
False
# 變數
name = "高木"
age = 14
is_female = True
# 1.變數的名稱只能是英文OR數字OR_的組合
# 2.變數的開頭不可以是數字

# 設變數，與其他字串一起print出來
print("有一個人叫" + name)
print(name + "喜歡捉弄西片")
name = "西片"
print("而" + name + "不喜歡被捉弄")
name = True
print(name)

# 如何使用字串、字串的用法
print("今天天氣很好\n鄰居請高木幫忙遛狗")
print("這隻狗叫\"Oreo\"")
color = "白色"
print("牠是隻" + color + "的大狗")

# 函式
dog_name = "Oreo"
#           0123
print(dog_name.lower().islower()) # 用於檢視大小寫
print(dog_name.upper().isupper())
print(dog_name.islower())
print(dog_name.isupper())

print(dog_name[1]) # 印出編號1的字
print(dog_name.index("o")) # 僅回傳最前面的字（假設有兩個o）
print(dog_name.replace("O","A")) # 替換字（會替換符合條件的所有字）

# 如何使用數字、數字的用法
from math import * #數學函式擴充包
print(8//5) # 無條件捨去小數點後數字
number=10
print((2+number)%5) # 餘數
print("後面應該會有數字，像是：" + str(number)) # 字串相加
number=-6
print(abs(number)) # 絕對值
print(pow(2,10)) # 次方
print(max(-1,3,5,7,9,99)) # 找最大的數
print(min(-1,3,5,7,9,99)) # 找最小的數
print(round(88.8)) # 四捨五入
print(floor(3.9)) # 無條件捨去
print(ceil(3.9)) # 無條件進位
print(sqrt(81))

# 建立一個基本計算機
number1 = input("請輸入第一個數字： ") #imput預設為字串()
number2 = input("請輸入第二個數字： ")
print(float(number1) + float(number2))
