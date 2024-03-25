#  def fibonaccis(i):
#     if i<=0:
#      return i
#     else:
#         return(fibonaccis(i-1) + fibonaccis(i-2))
# num=int(input("Enter"))
# if num<=0:
#     print("enter a +ve number")
# else:
#  print("fibonaccis:")
# for i in range(num):
#      print(fibonaccis(i))


num=10
n1,n2=0,1
print("fibonacci series of:",n1 ,n2)
for i in range(num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end="")