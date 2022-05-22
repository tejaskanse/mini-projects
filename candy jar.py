n = 50
print("number of candies available",n)
C = int(input("how many candies you want?"))
k = 5
if(C>n):
     print("invalid input")
     print("candies remain:", end=" ")
     print(n)
elif(C <= 0):
     print("invalid input")
     print("candies remain:", end=" ")
     print(n)
else:
     print("candies sold:", end=" ")
     print(C)
     print("candies remain:", end=" ")
     print(n-C)
