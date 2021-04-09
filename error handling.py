
x=42
y=0
try:
    print(x/y)
except ZeroDivisionError as e:
    print("sorry1")
except:
    print("sorry2")
finally:
    print('finally sorry')
    
