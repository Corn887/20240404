# 列表list、列表的用法
scores1 = [90,80,70,60,50]
print(scores1)
friends = ["西片","日々野 ミナ","月本 サナエ","天川 ユカリ"]
print(friends)
things = [14,"西片",True] #list可包含不同資料型別
print(things)
print(scores1[3])
print(scores1[-1])
print(scores1[2:4]) #從第x項開始取，取到y的前一項
print("--------------------------------------1")
print(scores1[1:]) #從第x項開始取(不含)
print(scores1[:4]) #從第x項開始取(不含)
ask = "今天天氣很好，鄰居請高木幫忙遛狗"
print(ask[0:6])
scores1[1] = 30 # 改list內數字
print(scores1)

scores1.extend(friends) # 擴增其他列表
print(scores1)

scores1.append(30) # 擴增其他值
print(scores1)

scores1.insert(2,100) # 插入值在x項，其餘向右推
print(scores1)

scores1.remove(90) # 刪除列表中某值
print(scores1)

scores1.pop() # 移除最後一項
print(scores1)

scores1.clear() # 清空列表
print(scores1)

print("--------------------------------------2")

scores2 = [20,40,60,80,30,60,90,100]
scores2.sort() # 由小到大排列
print(scores2)

scores2.reverse()
print(scores2) # 列表反轉

print(scores2.index(60)) # 印出特定值在第幾項，取最前面

print(scores2.count(60)) # 印出特定值在列表中出現幾次
print("--------------------------------------3")

# 元組tuple (一但創建後，就不能做新增、修改、刪除)
scores3 = (90,80,70,60,50)
print(scores3[:2]) # 同列表可取特定位置
print(len(scores3)) # 計算內含幾個值