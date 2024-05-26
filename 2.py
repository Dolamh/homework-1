def Func(b):
    dec=0
    l=[]
    try:
        for i in range(len(b)):
            t= int(b[i])
            dec += t * 2**(len(b)-i-1)
        return dec
    except Exception as e:
        print(e)
print("Bin To Dec Converter App")        
while True:
    b=input("Input an binary number OR enter x to exit: ")
    if b=='x':
        print("End")
        break
        
    d=Func(b)
    if d:
        print(d)
