#test3
score = float(input("请输入您的分数:"))
if score < 0 or score>1:
    print("输入错误")
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')