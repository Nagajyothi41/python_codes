# def basic():
#     print("hellow world")
# basic()

# def greet(name):
#     print("hellow "+name)
# greet("raju")

# def add(a,b):
#     print(a+b)
# add(3,6)

# def add_return(a,b):
#     return a+b 
# r=add_return(4,8)
# print(r)

# def even_odd(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "add"
# print(even_odd(15))

# def square(n):
#     return n*n 
# print(square(5))

# def maxa(a,b):
#     if a>b:
#         return a 
#     else:
#         return b 
# print(maxa(25,78))

# def greet(name="jyo"):
#     print("hellow "+name)
# greet()
# greet("raju")

# def emp(name,age,salary):
#     print(name)
#     print(age)
#     print(salary)
# emp("jyo",21,50000)

# def fac(n):
#     r=1
#     for i in range(1,n+1):
#         r=r*i 
#     return r 
# print(fac(5))

# def check(n):
#     if n>0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return "zero"
# print(check(-60))

# def p_i(p,r,t):
#     return (p*r*t)/100
# print(p_i(10000,5,2))

# def len_n(n):
#     return len(n)
# print(len_n("Python"))

# def avg(a,b,c):
#     return (a+b+c)/3  
# print(avg(3, 4,9))

# def opp(a,b):
#     add=a+b 
#     sub=a-b
#     mul=a*b 
#     return add,sub,mul 
# x,y,z=opp(2,3)
# print(x)
# print(y)
# print(z)

# def larg(num):
#     l=num[0]
#     for i in num:
#         if i>l:
#             l=i 
#     return l 
# num=[1,3,2,6,5]
# print(larg(num))

# def count(num):
#     c_even=0
#     c_odd=0 
#     for i in num:
#         if i%2==0:
#             c_even+=1 
#         else:
#             c_odd+=1 
#     return c_even,c_odd 
# num=[1,3,2,4,9]
# x,y=count(num)
# print(x)
# print(y)

# def dup(n):
#     r=[]
#     for i in n:
#         if i not in r:
#             r.append(i)
#     return r 
# n=[1,2,9,2,4,3,3]
# print(dup(n))

# def palin(s):
#     s=s.lower()
#     if s==s[::-1]:
#         return True 
#     else:
#         return False 
# print(palin("madam"))

# def bonus(salary,exp):
#     if exp>=10:
#         bonus=salary*0.20 
#     elif exp>=5:
#         bonus=salary*0.15 
#     else:
#         bonus=salary*0.10
#     return bonus 
# salary=100000
# exp=5
# print("bonus: ", bonus(salary,exp))

# def emp(name,depart,salary):
#     return f"name: {name},department :{depart},salary: {salary}"
# print(emp(name= "jyo", depart="IT", salary=200000))

# def summ(*n):  ##*args
#     smm=0 
#     for i in n:
#         smm+=i 
#     return smm 
# print(summ(10,1,2,22,433,))

# def key_value(**n):
#     for key,value in n.items():
#         print(key, ":" , value)
# key_value(name="jyo",salary="50000",dap="it")




# def student_result(name, marks):
#     total = sum(marks)
#     average = total / len(marks)

#     if average >= 60:
#         result = "Pass"
#     else:
#         result = "Fail"

#     return {
#         "Name": name,
#         "Total": total,
#         "Average": average,
#         "Result": result
#     }


# student = student_result("Ravi", [75, 80, 65])

# print(student)

def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(amount):
    if amount >= 10000:
        return amount * 0.10
    elif amount >= 5000:
        return amount * 0.05
    else:
        return 0


def final_amount(price, quantity):
    total = calculate_total(price, quantity)
    discount = calculate_discount(total)

    return total - discount


print(final_amount(3000, 4))

