# 請使用者輸入身高及體重，並將其轉換為浮點數以進行運算
height_cm_input = input("你的身高是(cm)：")
height_cm = float(height_cm_input)
weight_kg_input = input("你的體重是(kg)：")
weight_kg = float(weight_kg_input)

# BMI的運算過程 + 簡化數字
height_m = height_cm/100
BMI_initial = weight_kg/pow(height_m,2)
BMI = round(BMI_initial,2)   # 四捨五入至小數點後第二位

# 分析BMI的意義
show = "你的BMI為：" + str(BMI) + " 屬於"
if 35 <= BMI:
    print(show + "重度肥胖")
elif 30 <= BMI < 35:
    print(show + "中度肥胖")
elif 27 <= BMI < 30:
    print(show + "輕度肥胖")
elif 24 <= BMI < 27:
    print(show + "過重")
elif 18.5 <= BMI < 24:
    print(show + "正常範圍")
else:
    print(show + "體重過輕")
