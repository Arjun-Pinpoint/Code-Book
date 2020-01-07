# 1. check whether a number is positive or negetive or zero
num=input()
try:
    num=float(num)
    if num>0:
        print("Positive")
    elif num<0:
        print("Negative")   
    else:
        print("Zero")
except:
    print("Invalied Input")
