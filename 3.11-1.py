#test1
hours = int(input("请输入时长:"))
rate = int(input("请输入速率:"))
payMoney=hours*rate
if hours>40:
    payMoney+=0.5*rate*(hours-40)
    print(payMoney)
else:print(payMoney)
