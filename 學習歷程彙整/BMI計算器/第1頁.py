# 請使用者輸入身高及體重，並將其轉換為浮點數以進行運算
height_cm = float(input("你的身高是(cm)："))

weight_kg = float(input("你的體重是(kg)："))

# BMI的運算過程 + 簡化數字
height_m = height_cm/100
BMI_initial = weight_kg/pow(height_m,2)   # pow用來取平方
BMI = round(BMI_initial,2)   # 四捨五入至小數點後第二位

# 分析BMI的意義
show = "你的BMI為：" + str(BMI)
if 35 <= BMI:
    print(show + " 屬於重度肥胖")
elif 30 <= BMI < 35:
    print(show + " 屬於中度肥胖")
elif 27 <= BMI < 30:
    print(show + " 屬於輕度肥胖")
elif 24 <= BMI < 27:
    print(show + " 屬於過重")
elif 18.5 <= BMI < 24:
    print(show + " 屬於正常範圍")
else:
    print(show + " 屬於體重過輕")