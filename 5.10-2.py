i=1
while 1:
    n = input("Enter a number：")
    if n == 'done':
        break
    try:
        m = int(n)
        if i==1:
            min = max = m
        if max<m:
            max=m
        if min>m:
            min=m
        i=0
    except:
        print("Invalid input")
print("maximum:",max,"minimum:",min)