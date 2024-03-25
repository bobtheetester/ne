def fibonaccis(i):
    if i<=0:
     return i
    else:
        return(fibonaccis(i-1) + fibonaccis(i-2))
num=int(input("Enter"))
if num<=0:
    print("enter a +ve number")
else:
 print("fibonaccis:")
for i in range(num):
    print(fibonaccis(i))