# # prime number 
# def num(n):
#     if n<=1:
#         return False
#     i=2
#     while i<n:
#         if n%i==0:
#             return False
#         i+=1 
#     return True 
# n=int(input("enter: "))
# if num(n):
#     print("prime")
# else:
#     print("not prime")

## factorial number 
# def num(n):
#     r=1
#     for i in range(1,n+1):
#         r=r*i 
        
#     return r 
# n=int(input("enter: "))
# print(num(n)) 

## reverse number, string
# def num(n): #number
    
#     r=0 
#     while n>0:
#         digit=(n)%10 
#         r=r*10+digit 
#         n//=10 
#     return r 
# n=int(input("enter: "))
# print(num(n))

# def num(n):
#     s=""
#     for i in n:
#         s=i+s 
#     return s 
# n=(input("enter: "))
# print(num(n))

## palindrome 
