#!/usr/bin/env python
# coding: utf-8

# # 1. Variables and data types

# In[1]:


print("Hello Yash Sharma")


# In[9]:


a=15
print(a,type(a))


# In[11]:


b=12
c=13.5
print(b,type(c))


# In[13]:


d='yash sharma'
print(d,type(d))


# In[15]:


e='''plot no. 05,green park colony,gudha road,bandikui.'''
print(e,type(e))


# # 2. Input and type casting

# In[3]:


a=input("Enter your first name: ")
b=input("Enter your middle name: ")
c=input("Enter your last name: ")
d=a+b+c
print(d)


# In[4]:


a=input("Enter your first name: ")
b=input("Enter your middle name: ")
c=input("Enter your last name: ")
d=a+" "+b+" "+c
print(d)


# In[5]:


a


# In[6]:


b


# In[7]:


c


# In[8]:


id(a)


# In[9]:


id(b)


# In[10]:


id(c)


# In[18]:


a=input("Enter a: ")
b=input("Enter b: ")
c=a+b
print(c)


# In[ ]:


# 18 no. row m input function k ander string value store h issliye is function ko run krne pr y hme same value print krke deta h.


# In[13]:


a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=a+b
print(c)


# In[14]:


a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=a+b
print(c)


# In[15]:


a=complex(input("Enter a: "))
b=complex(input("Enter b: "))
c=a+b
print(c)


# In[ ]:


# Agar kisi bhi function m kis type ki value store h pta krna h to "eval function" ka use krte h.


# In[19]:


a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
c=a+b
print(c)


# # Task 1

# In[22]:


name=input("Enter your name: ")
print("hello",name,",","how are you?")


# In[23]:


name=input("Enter your name: ")
print(f"Hello {name},how are you?")


# In[1]:


a=input("Enter your name: ")
print(f"May i help you,{a}?")


# # Operaters:-

# In[22]:


# operators are 7 types:-
#1. Arithmatic Operator
#2. Assignment Operator
#3. Comparision Operator
#4. Logical Operator
#5. Bitwise Operator
#6. Identity Operator
#7. Membership operator


# # 1. Arithmatic Operator:-

# In[5]:


#1. Arithmatic Operator are 7 types:-
#a= +
#b= -
#c= *
#d= / (Float Division)
#e= // (Floor Division)
#f= % (Modulus)
#g= ** (power)


# # some Examples:-

# In[6]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
add = a+b
print(add)


# In[8]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
sub = a-b
print(sub)


# In[10]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
mul = a*b
print(mul)


# In[16]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
float_division = a/b
print(float_division)


# In[17]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
floor_division = a//b
print(floor_division)


# In[18]:


# Row 16 and 17 Float division m point k baad ki value bhi print karta h but floor division actual value ko hi print karta h.


# In[20]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
mod = a%b
print(mod)


# In[21]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
power = a**b
print(power)


# # 2. Assignment Operator:-

# #some Examples:-

# # a=a+b or a+=b   Otherwise  a=a-b  or a-=b

# In[25]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
a = a+b                                 # Otherwise a+=b bhi likh sakte h.
print(a)
print(b)


# In[27]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
a-=b
print(a)
print(b)


# #  3. Comparison operator:- 

# In[30]:


# This is 6 types:- 
#1. <= (Less than)
#2. <= (less than Equal to)
#3. >= (Greater than)
#4. >= (Greater than Equal to)
#5. == (Equal to)
#6> != (Not equal to)


# # Some Examples:-

# In[31]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
print(a<b)


# In[33]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
print(a>=b)


# In[34]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
print(a==b)


# In[36]:


a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
print(a!=b)


# # 4. Logical Operator:-

# In[2]:


# This is 3 types:-
# 1. and
# 2. or
# 3. not


# # Example (and):-

# In[ ]:


# and operator me agar ek bhi condition false ho to result bhi false hi aata h.


# In[ ]:


a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
c=(a<b) and (a!=b)
print(c)


# In[6]:


a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
c=(a>b) and (a!=b)
print(c)


# # Example (or):-

# In[ ]:


# or operator ka use agar ek bhi condition true hoti h to result true aata h.


# In[ ]:


a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
c=(a<b) or (a!=b)
print(c)


# In[4]:


a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
c=(a>b) and (a!=b)
print(c)


# # Example(not):-

# In[1]:


a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
c=not((a<b) and (a!=b))
print(c)


# In[3]:


a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
c=not((a<b) or (a!=b))
print(c)


# # 5. Membership Operator(in / not in):-

# In[8]:


a="yash kumar sharma"


# In[9]:


"yas" in a


# In[16]:


"sharma " in a


# In[14]:


"kumar" not in a


# # 6. Bitwise Operator:-

# In[15]:


# This is 3 types:-
# 1. & - and
# 2. | - or
# 3. ~ - not


# # Example:-

# In[17]:


a=4
b=8
c=a&b
print(c,type(c))


# In[18]:


a=4
b=8
c=a|b
print(c,type(c))


# In[20]:


a=4
b=8
c=~a
print(c,type(c))


# In[21]:


a=4
b=8
c=~b
print(c,type(c))


# # If - else:-

# In[1]:


# Some Examples:-


# In[2]:


face=input("Enter the face of coin: ")
if face=="head":
    print("win")
else:
    print("loose")


# In[4]:


face=input("Enter the face of coin: ")
if face=="head":
    print("win")
elif face=="tail":
    print("loose")
else:
    print("Invalid syntex")


# In[5]:


# Signal light example:-


# In[8]:


t_light = input("Enter the colour of light: ")
if t_light=="Red":
    print("Please stop.")
elif t_light=="yellow":
    print("Ready to go.")
elif t_light=="Green":
    print("Please go.")
else:
    print("Invalid Syntex")


# In[9]:


# Odd - Even No. Example:-


# In[11]:


number = int(input("Enter a number: "))
if number%2==0:
    print(number,"is even number.")
else:
    print(number,"is odd number.")


# In[12]:


number = int(input("Enter a number: "))
if number%2==0:
    print(number,"is even number.")
else:
    print(number,"is odd number.")


# In[13]:


# which is greater number:-


# In[14]:


a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a>b:
    print(a,"greater than",b)
elif a==b:
    print(a,"is equals to",b)
else:
    prnt(a,"is less than",b)


# In[15]:


a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a>b:
    print(a,"greater than",b)
elif a==b:
    print(a,"is equals to",b)
else:
    prnt(a,"is less than",b)


# In[16]:


a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a>b:
    print(a,"greater than",b)
elif a==b:
    print(a,"is equals to",b)
else:
    prnt(a,"is less than",b)


# # CALCULATER:-

# In[19]:


a = eval(input("Enter a: "))
opr = input("Enter the operater: ")
b = eval(input("Enter b: "))
if opr=="+":
    print(a,"+",b,"=",a+b)
elif opr=="-":
    print(a,"-",b,"=",a-b)
elif opr=="*":
    print(a,"*",b,"=",a*b)
elif opr=="/":# {/ = float division}:
    print(a,"/",b,"=",a/b)
elif opr=="//": #{// = floor}:
    print(a,"//",b,"=",a//b)
elif opr=="**":
    print(a,"**",b,"=",a**b)
elif opr=="%":
    print(a,"%",b,"=",a%b)
else:
    print("Invalid Syntex")
    


# In[25]:


a = eval(input("Enter a: "))
opr = input("Enter the operater: ")
b = eval(input("Enter b: "))
if opr=="+":
    print(a,"+",b,"=",a+b)
elif opr=="-":
    print(a,"-",b,"=",a-b)
elif opr=="*":
    print(a,"*",b,"=",a*b)
elif opr=="/":# {/ = float division}:
    print(a,"/",b,"=",a/b)
elif opr=="//": #{// = floor}:
    print(a,"//",b,"=",a//b)
elif opr=="**":
    print(a,"**",b,"=",a**b)
elif opr=="%":
    print(a,"%",b,"=",a%b)
else:
    print("Invalid Syntex")
    


# In[26]:


# Leap year or Aleap year:
# condition 1:- Leap year hone k liye vo number 400 se or 100 se dono se divisible hona chaiye.
# condition 2:- leap year hone k liye vo number 4 se to divisible ho lakin 100 se divisible nhi hona chaiye.


# In[27]:


year = int(input("Enter the year: "))
if (year/400==0) and (year/100==0):
    print(year,"in a leap year.")
elif (year/4==0) and (year/100!=0):
    print(year,"in a leap year.")
else:
    print(year,"not a leap year.")


# In[37]:


year = int(input("Enter the year: "))
if (year/400==0) and (year/100==0):
    print(year,"in a leap year.")
elif (year/4==0) and (year/100!=0):
    print(year,"in a leap year.")
else:
    print(year,"not a leap year.")


# # Loops:- 

# In[38]:


# loops are 2 types:- 
# 1. For loop (sequence and range function)
# 2. While loop


# In[39]:


# Range m 3 points hote h:- 
# 1. starting point(By Default = 0)
# 2. Ending point
# 3. Updation (By Default = 1)


# # Loops in python:- 

# In[40]:


for i in range(5):
    print(i)


# In[41]:


for i in range(2,10):
    print(i)


# In[44]:


for i in range(2,21,2):
    print(i)


# In[46]:


for i in range(2,21,2):
    print(i,end=" ")


# In[47]:


for i in range(2,21,3):
    print(i,end=" ")


# # How to create tables in loop:-

# # 1. for loop:-

# In[1]:


n=5
for i in range(1,11):
    print(n*i)


# In[3]:


n=int(input("Enter a number: "))
for i in range(1,11):
    print(n*i)


# In[4]:


n=int(input("Enter a number: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)


# # 2. while loop:-

# In[1]:


n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1


# # how to find any number of square:-

# In[4]:


n=eval(input("Enter a number: "))
sqrt = n**(0.5)
print(sqrt)


# # 2. method

# In[6]:


n=eval(input("Enter a number: "))
import cmath
sqrt = cmath.sqrt(n)
print(sqrt)


# # Area of circle = pai(22/7)*r^2

# In[10]:


rad = float(input("Enter the radius of circle: "))
area = (22/7)*rad*rad
print(area)


# In[16]:


# Area of triangle(hero's Formula) = ((s)*(s-a)*(s-b)*(s-c))**(0.5)
# s= a+b+c/2


# In[18]:


a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
c=int(input("Enter side c: "))
s=a+b+c/2
area = ((s)*(s-a)*(s-b)*(s-c))**(0.5)
print(area)


# # # quardatic equation = a*x^2+b*x+c=0
# 

# In[21]:


a=eval(input("Enter side a: "))
b=eval(input("Enter side b: "))
c=eval(input("Enter side c: "))
d=((b*b-4*a*c))**(0.5)
x1=((-b)+(d))/(2*a)
x2=((-b)-(d))/(2*a)
print(x1)
print(x2)


# # Task:-

# In[24]:


a=input("Enter your name: ")
b=input("Enter your age: ")
c=input("Enter your city: ")
print("Hello my name is",a,".","I am",b,"years old and I am from",c)


# In[25]:


a=input("Enter your name: ")
b=input("Enter your age: ")
c=input("Enter your city: ")
print(f"Hello my name is {a},I am {b} years old and I am from {c}")


# In[1]:


name="Yash sharma"
for i in name:
    print(i)


# In[2]:


name="Yash sharma"
for i in name:
    print(i,end=" ")


# In[3]:


len(name)


# In[4]:


# list(l)
l=[12,"yash sharma",25+2j,26.3]
for i in l:
    print(i)


# In[5]:


len(l)


# In[7]:


# tuple(t)
t=(10.5,"yash",10+26j)
for i in t:
    print(i)


# In[8]:


len(t)


# # + ke liye = 0
# # *  ke liye = 1

# In[24]:


# New Topic:-
# 1. by for loop:-


# In[15]:


n=int(input("Enter a number: "))
# let c=Container
c=0
for i in range(1,n+1):
    c+=i
print(c)


# In[16]:


# 2. By while loop:-


# In[17]:


n=int(input("Enter a number: "))
c=0
i=1
while i<=n:
    c+=i
    i+=1
print(c)


# In[18]:


# 3. By formula se:-


# In[20]:


n=int(input("Enter a number: "))
s=((n)*(n+1))/2
print(s)


# In[21]:


# By other method:-


# In[23]:


n=int(input("Enter a number: "))
c=sum(range(1,n+1))
print(c)


# # How to find any number of factorial:-

# In[26]:


# 1. By for loop:-


# In[25]:


number=int(input("Enter a number: "))
c=1
for i in range(1,number+1):
    c*=i
print(c)


# In[27]:


# 2. By while loop:-


# In[3]:


number=int(input("Enter a number: "))
c=1
i=1
while i<=number:
    c*=i
    i+=1
print(c)


# # Nested If - else :-

# In[1]:


# online payment :-(Single person)

card=input("Enter the type of card: ")
if card in ["credit","debit"]:
    print("vaild card ")
    card_number=input("Ente the number of card:  ")
    if card_number=="1234567890":
        print("valid card number" )
        name=input("Enter your name: ")
        if name=="Yash":
            print("Valid user ")
            cvv=int(input("Enter your cvv: "))
            if cvv==123:
                print("Card verified")
                amt=int(input("Enter your amount: "))
                print("Hello",name,"please collect your amount of",amt,"rupees.")
            else:
                print("invalid cvv")
        else:
            print("invalid user")
    else:
        print("invalid card number.")
else:
    print("invalid card")
    


# # Fibbonacci series using for loop:-

# In[8]:


# 

term=int(input("Enter the terms: "))
a=0
b=1
c=0
for i in range(term):
    print(c,end=" ")
    a=b
    b=c
    c=a+b


# # Fibonacci series using while loop: 

# In[2]:


# 
term=int(input("Enter the number of terms: "))
a=0
b=1
c=0
i=1
while i<=term:
    print(c,end=" ")
    a=b
    b=c
    c=a+b
    i+=1


# In[ ]:





# # Palindrome number using for loop:- 

# In[4]:


number=int(input("Enter the number: "))
copy=number
order=len(str(number))
new=0

for i in range(order):
    digit=number%10
    new=new*10+digit
    number=number//10

if copy==new:
    print(copy,"is palindorme number.")
else:
    print(copy,"is not palindrome number.")


# # Palindrone number using while loop:- 

# In[9]:


number=int(input("Enter the number: "))
copy=number
order=len(str(number))
new=0
i=1
while i<=order:
    digit=number%10
    new=new*10+digit
    number=number//10
    i+=1
if copy==new:
    print(copy,"is palindrome number.")
else:
    print(copy,"is not a palindrome number.")


# # Armstronge number using for loop:-

# In[10]:


number=int(input("Enter the number: "))
copy=number
order=len(str(number))
new=0
for i in range(order):
    digit=number%10
    new=new+digit**order
    number=number//10
if copy==new:
    print(copy,"is armstronge number.")
else:
    print(copy,"is not a armstronge number.")


# # Armstronge number using while loop:-

# In[7]:


number=int(input(("Enter the number: ")))
copy=number
order=len(str(number))
new=0
i=1
while i<=order:
    digit=number%10
    new=new+digit**order
    number=number//10
    i+=1
if copy==new:
    print(copy,"is armstronge number.")
else:
    print(copy,"is not a armstronge number.")


# # Homogenious and Hetrogenious:-

# In[ ]:


# 1. list
# 2. tuple
# 3. dict (Dictionary)
# 4. set


# In[ ]:


# Data types :- 2 types

# 1. mutable data type
# 2. immutable data type


# # 1---: List :-

# In[9]:


# Index:-

l=[12,35,45,"yash sharma",10+5j,True]


# In[10]:


l


# In[11]:


type(l)


# In[16]:


#  list m first value zero(0) se start hoti h fir one(1),2,3,4,..........................chalta rhta h.(Positive Direction)
#  list m back side se first value -1hoti h or isi tarah -1,-2,-3,-4.....................chalta rhta h.(Negative Direction)


# In[14]:


l[5]


# In[15]:


l[3]


# In[17]:


l[-3]


# In[18]:


l[-2]


# In[22]:


l[0:5:2]


# In[23]:


l[1]=80


# In[24]:


l


# In[25]:


for i in l:
    print(i)


# In[26]:


len(l)


# In[28]:


l=[i for i in range(1,21)]


# In[29]:


l


# In[30]:


a=[k for k in range(2,21,2)]


# In[31]:


a


# # Operations without methods:-

# In[33]:


a=[14,19,True,95]
b=[48,25,16,"yash sharma"]


# In[34]:


a>b


# In[35]:


a=["yash"]
b=['SOHIL']


# In[36]:


a<b


# # ASCII Values:- 

# In[41]:


ord("a") 


# In[39]:


ord("A")


# In[43]:


ord("y")


# In[44]:


ord("s")


# In[45]:


chr(97)


# In[46]:


chr(65)


# In[47]:


a=["yash"]
b=["sharma"]


# In[48]:


c=a+b


# In[49]:


c


# # 2 ---: Tuple:-

# In[1]:


t=(12,25,36,58+2j,2.6,True,"yash")


# In[2]:


type(t)


# In[3]:


id(t)


# In[4]:


# Indexing :-

t[1]


# In[5]:


t[5]


# In[6]:


t[-2]


# In[7]:


# note :- indexing krte time t k aage square bracket m index value dete h.


# In[8]:


t[2::2]


# In[10]:


t[::-1] # tuple ko reverse order m bhi likh sakte h.


# In[13]:


# first method:-


# In[12]:


for i in t:
    print(i)


# In[14]:


# second method:-


# In[15]:


for i in range(len(t)):
    print(t[i])


# In[16]:


# membership operator:-

25 in t


# In[17]:


34 in t


#  # Nested tuple:-

# In[37]:


a=(15,59,35,'yash',("sohan",52,58),("vaishali","aryan",(58,89)))


# In[38]:


a[3]


# In[39]:


a[4][0]


# In[40]:


a[4]


# In[41]:


a[5][1]


# In[42]:


a[5][2][1]


# In[43]:


l=[10]


# In[44]:


type(l)


# In[45]:


t=(10)


# In[46]:


type(t)


# In[48]:


t=(10,)


# In[49]:


type(t)


# In[50]:


a=15,


# In[51]:


type(a)


# # Operation without methods:-

# In[52]:


a=(23,58,26,45,85)
b=(56,48,62,94,75)


# In[53]:


a<b


# In[55]:


# tuple hamesha first value m comparision krta h.
# 23 or 56 m 56 greater h isiliye result True aaya h.
# tuple m string - string or integer - integer ka comparision ho sakta h.
# tuple m kbhi string - intiger ka comparison nhi hota h.


# In[56]:


c=("yash",42)
d=("vinay","kumar")


# In[57]:


c<d


# In[59]:


# Is example m string k first character ka comparision hoga or isski value (Accii value) se nikalte h.
ord("y")


# In[63]:


ord("v")


# In[64]:


# v ki value greater h.


# In[66]:


# Concatination:-

a=(23,85,56,49,45)
b=(58,75)


# In[67]:


a+b


# In[68]:


# Replication:-

a=(23,85,56,49,45)


# In[69]:


a*2


# #                                       Tuple Methods:-

# In[2]:


a=(25,65,36,75,53)


# In[4]:


id(a)            


# In[5]:


a=a*2


# In[6]:


a


# In[8]:


id(a)                      #isme a ki ID change ho gyi.


# In[9]:


# tuple methods:- 


# In[10]:


t=(13,25,"sharma",10+2j,True,10.3)


# In[11]:


t.index(25)


# In[15]:


id(t)


# In[19]:


t.index(25,10.3,0)


# In[20]:


t.count(25)


# In[21]:


t.count(100)


# In[22]:


t=(34,58,56,28,42,65)


# In[23]:


sorted(t)


# In[24]:


id(t)


# In[27]:


t=sorted(t)


# In[28]:


t


# In[30]:


id(t)                         # ID change ho jayegi.


# In[31]:


sorted(t,reverse=True)


# In[34]:


del t[2]


# In[35]:


t


# In[39]:


del t[::2]


# In[41]:


t


# In[42]:


del t


# In[43]:


t


# In[44]:


a=(25.86,18,56,54,28.2,65.1,58.4)


# In[45]:


min(a)


# In[46]:


max(a)


# In[47]:


sum(a)


# # Packing - Unpacking of a tuple : -

# In[52]:


# First method:-


# In[48]:


a=(15,"sharma",59,48,75)


# In[50]:


p,q,r,s,t=a
q=45
a=(p,q,r,s,t)


# In[51]:


a


# In[53]:


# Second Method :-


# In[54]:


# Phle values ko list mai convert karenge than jo bhi element add krna ho use add krke use dubara tuple m convert kar denge.


# In[55]:


l=list(a)


# In[56]:


l


# In[57]:


l.append("sharma")


# In[58]:


l


# In[59]:


a=tuple(l)


# In[60]:


a


# In[61]:


l=list(a)


# In[64]:


l[1]="verma"


# In[65]:


a=tuple(l)


# In[66]:


a


# #  Colorama : -

# In[13]:


import colorama
from colorama import Fore,Back,Style


# In[23]:


print(Fore.MAGENTA+Back.LIGHTWHITE_EX+Style.NORMAL+"12345")


# In[26]:


print(Fore.LIGHTYELLOW_EX+Back.LIGHTBLACK_EX+Style.DIM+"yash sharma")


# # ======================(Use of "\n" and "\t" ) :-

# In[27]:


print("yash sharma")


# In[28]:


print("I am 23 yers old.")


# In[29]:


print("I am from jaipur.")


# # condition 1 :- "\n" ka use new line k liye kiya jata h.

# In[35]:


print("My name is yash sharma\nI am 23 years old\nIam from jaipur.")


# In[36]:


# condition 2 :- "t" ka use space dene k liye kiya jata h.


# In[38]:


print("yash\t\t\t\t\t\t\t\t\t\t sharma")


# In[40]:


print(Fore.LIGHTRED_EX+Back.YELLOW+Style.BRIGHT+"Use of 'PANDAS LIBRERY'.")


# # PANDAS LIBRERY:-

# In[9]:


roll_number=list(map(int,input("Enter the roll number: ").split()))
name=list(input("Enter the name: ").split())
department=list(input("Enter the department neme: ").split())
Gender=list(input("Enter the gender: ").split())
age=list(map(int,input("Enter the age: ").split()))
city=list(input("Enter the city: ").split())


# In[10]:


Info={"Roll Number":roll_number,"Name":name,"Department":department,"gender":Gender,"Age":age,"Address":city}


# In[12]:


import pandas as pd
df=pd.DataFrame(Info)


# In[13]:


df


# # SETS :-

# In[25]:


s={12,25,36,25,15,29,95,63}


# In[26]:


len(s)


# In[27]:


# set m kbhi bhi repeate element count nhi hota h.


# In[29]:


for i in s:
    print(i,end=" ")


# In[30]:


s1={i for i in range(1,21)}


# In[31]:


s1


# In[32]:


type(s1)


# In[33]:


t=()


# In[34]:


type(t)


# In[1]:


l=[]


# In[3]:


type(l)


# In[5]:


d={}


# In[6]:


type(d)


# In[7]:


s=set({})


# In[8]:


type(s)


# In[10]:


s1={25,35,65,58+2j,52,True,False,95,7}
s2={35,65,"sharma"}


# In[11]:


# 1. Union/Update  :-


# In[12]:


s1.union(s2)


# In[13]:


id(s1)


# In[14]:


id(s2)


# In[15]:


s1.update(s2)


# In[16]:


s1


# In[17]:


id(s1)


# In[18]:


# 2. Intersection/Intersection_update() :-


# In[19]:


s1


# In[20]:


s2


# In[21]:


s1.intersection(s2)


# In[22]:


# if Update s1 then use this:-

s1.intersection_update(s2)


# In[23]:


s1


# In[24]:


id(s1)


# In[25]:


# 3. Differance/Differance_update() :-


# In[29]:


print(f"{s1} \n{s2}")


# In[30]:


s1-s2


# In[31]:


s1


# In[33]:


# if s1 update s2 then use this:-

s1.difference_update(s2)


# In[34]:


s1


# In[35]:


s2


# In[36]:


# 4. Symmetric_difference/Symmetric_difference_update :-


# In[38]:


a={12,52,85,64+5j,58,65}
b={15,85,45,68,"yash"}


# In[39]:


a.symmetric_difference(b)


# In[40]:


# a ko b se update krne k liye :-


# In[41]:


a.symmetric_difference_update(b)


# In[42]:


a


# In[43]:


# 5. Disjoint set :- {when all elements are not same of a and b}


# In[45]:


a.isdisjoint(b)


# In[46]:


# 6. Subset :-


# In[47]:


a.issubset(b)


# In[48]:


b.issubset(a)


# In[51]:


# Superset:- {jab b ke sare elements a m ho to a,b ka superset hoga}


# In[52]:


c={52,65,35,32,95,56,25}
d={52,35,56}


# In[53]:


c.issuperset(d)


# In[54]:


d.issuperset(c)


# In[55]:


# Add() :-


# In[57]:


c


# In[59]:


c.add(20)


# In[60]:


c


# # Pop Method() :- (pop method fuction k kisi bhi element ko return krke remove krta h)

# In[61]:


c


# In[63]:


c.pop()


# In[64]:


c


# # Remove/Discard() Method :- 

# In[65]:


c


# In[66]:


c.remove(20)


# In[67]:


c


# In[68]:


c.discard(53)


# In[69]:


c


# In[70]:


# remove method m yadi ham function k kisi bhi element ko delete krte h to vo element us function m hona chaiye vrna error show hoga.
# lakin yadi discard method m function m jo element nhi h use remove kr rhe h vo y hme koi error nhi deta h.


# In[71]:


c.remove(26)


# In[72]:


c.discard(26)


# In[73]:


c


# In[74]:


# Clear method :-


# In[76]:


c.clear()


# In[77]:


c


# In[78]:


# set ko bhi delete krne k liye del function ka use krte h.


# In[79]:


del c


# In[80]:


c


# # STRING() :- Most imp.

# In[81]:


a="yash sharma"


# In[82]:


a[3]


# In[83]:


a[-2]


# In[84]:


a[1:-3:2]


# In[85]:


a[::-1]


# In[86]:


# loop chalene k liye:-


# In[90]:


for i in a:
    print(i,end=" ")                # By first method:-


# In[91]:


len(a)


# In[95]:


for i in range(len(a)):
    print(a[i],end=" ")              #By Second method:-


# In[97]:


a[0]=t


# In[98]:


"yash" in a


# In[99]:


# Operation Without methods :-


# In[100]:


a="yash"
b="sharma"


# In[101]:


a>b


# In[106]:


ord("a")


# In[107]:


ord("S")


# In[108]:


a+' '+b


# In[116]:


a*3


# In[118]:


# METHODS :-


# In[119]:


name="yash sharma"


# In[120]:


name.upper()


# In[121]:


name.lower()


# In[122]:


name.capitalize()


# In[123]:


name.title()


# In[124]:


name.swapcase()


# In[125]:


a="YasH sHarMa"


# In[126]:


a.swapcase()


# In[127]:


# swapcase element k alphabates ko opposite order m kr deta h.


# In[128]:


name.isupper()


# In[129]:


name.islower()


# In[130]:


name.istitle()


# In[131]:


b=" "


# In[132]:


b.isspace()


# In[133]:


a.isalpha()


# In[153]:


c="12345"


# In[156]:


c.isalnum()


# In[155]:


c.isdigit()


# In[162]:


name=" yash sharma "


# In[164]:


name.strip()


# In[165]:


#  strip function string k aage or piche ka space htane k liye use kiya jata h


# In[166]:


name.lstrip()


# In[168]:


name.rstrip()


# In[173]:


name.rstrip("ma ")


# In[174]:


name=name.strip()


# In[175]:


name.index("k")


# In[179]:


name.find("k") 
# find method kisi bhi element ko dhundne ke kaam aata h agar vo element usme hota h to result dedeta h vrna -1 deta h.


# In[182]:


name.count("y")


# In[185]:


name.replace("s","$")


# In[188]:


name.endswith("rma ") # false issiliye aaya h kyuki last m space nhi h or yha space diya h.


# In[189]:


name


# # Break and Continue Statement --:

# In[13]:


# 1. Break statements:-


# In[12]:


# By For loop:-


# In[6]:


for i in range(5):
    n=int(input("Enter a number:  "))
    if n<0:
        print("loop ends.")
        break
    print(n)


# In[8]:


# By while loop:-


# In[11]:


i=1
while i<=5:
    n=int(input("Enter the number:  "))
    if n<0:
        print("loop ends.")
        break
    
    print(n)
    i+=1


# In[14]:


# 2. Continue statements:-


# In[15]:


# By for loop:-


# In[22]:


for i in range(5):
    n=int(input("Enter the number:  "))
    if n<0:
        print("This is skipped.")
        continue
    print(n)


# In[23]:


# 2. By while loop:-


# i=1
# while i<=5:
#     n=int(input("Enter the number:  "))
#     if n<0:
#         print("This is skipped")
#     i+=1
#     continue
# print(n)

# # How to Find Prime Number:-   VVM

# In[10]:


n=int(input("Enter the number:  "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"not a prime number.")
            break
    else:
        print(n,"prime number.")
else:
    print(n,"not a prime number.")


# # How to Find Odd-Even number :- VVM

# In[14]:


l=list(map(int,input("Enter the elements:  ").split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print("Even list-->",e)
print("Odd list-->",o)


# # Function:-

# In[15]:


# syntex :- for user defined function:
#             def fun_name(Parameter):
#               code and statement


# # Arguements:-   (5 types)

# In[16]:


# 1. Required arguments
# 2. Default arguments
# 3. Variable arguments
# 4. Keyword arguments
# 5. Variable length arguments


# In[17]:


def add():
    a=10
    b=20
    c=a+b
    print(c)                             # First Method


# In[21]:


add()


# In[22]:


def add(a,b):
    c=a+b
    print(c)                             # Second Method


# In[25]:


add(30,55)


# In[26]:


add()


# In[27]:


def add(a=10,b=53):
    c=a+b
    print(c)                             # Third Method


# In[28]:


add()


# In[29]:


add(25,30)


# In[31]:


add(50)            # By default b=53 lega.


# In[32]:


add(,12)           # By defalt a define nhi krega.


# In[34]:


add(b=10)            # yha By default a=10 lega.


# In[35]:


add(b=45,a=30)


# In[43]:


def add(*arg):                  # yha (*) list ko tuple m change kr deta h.
    a=0
    for i in arg:                      # (agr = Argument)
        a+=i
    print(a)                          # Forth Method


# In[44]:


add(10,20,30)


# In[45]:


def add(a=10,b=20):
    c=a+b
    print(c)                             # Fifth Method


# In[46]:


add()


# In[47]:


print(add())


# In[48]:


type(add())


# In[49]:


def add(a=10,b=30):
    c=a+b
    return c


# In[50]:


add()


# In[51]:


print(add())


# In[52]:


type(add())


# In[54]:


def add(a=10,b=50):
    c=a+b
    print("Hello")
    print("How are you?")
    return c


# In[55]:


add()


# In[56]:


# Return keyword,only function m hi use hota h or ek function m ek baar hi use hota h.
# Return k bad kuch bhi print nhi kr sakte.


# In[57]:


def add(a=20,b=50):
    c=a+b
    print("Hello")
    return c,a,"hello"
    print("How are you?")


# In[58]:


add()


# # Sum of Nutrals():-

# In[63]:


def sum_of_nutrals(n):
    a=0
    for i in range(1,n+1):
        a+=i
    print(a)                        


# In[66]:


sum_of_nutrals(5)                  # n=5, 1+2+3+4+5=15


# In[67]:


sum_of_nutrals(10)


# # Factorial By self code:-

# In[70]:


def fact(n):
    a=1
    for i in range(1,n+1):
        a*=i
    print(a)


# In[73]:


fact(5)                 # 5! = 5*4*3*2*1 = 120


# In[74]:


fact(8)


# # Odd - Even Numbers :-

# In[75]:


def even_odd(n):
    if n%2==0:
        return(f"{n} is even number.")
    else:
        return(f"{n} is odd number.")


# In[76]:


even_odd(55)


# In[77]:


even_odd(28)


# In[79]:


type(even_odd(52))


# # Most Topic--:  LAMBDA FUNCTION :-

# In[82]:


# Syntex:- lambda arguments:expression

lambda x,y:print(x+y)


# In[83]:


(lambda x,y:print(x+y))(2,3)


# In[85]:


(lambda x,y:print(x+y))(5,7)


# In[86]:


add=lambda x,y:print(x+y)


# In[87]:


add(7,9)


# In[88]:


add


# In[89]:


ab=lambda name,age,address :print(f"my name is {name},I am from {address},and I am {age} years old.")


# In[92]:


ab("Yash sharma",22,"Jaipur")


# In[93]:


type(ab)


# In[94]:


ab=lambda a,b,c,d,e,f:a+b-c*d/e**f


# In[95]:


ab(1,2,3,4,5,6)


# In[99]:


ab=lambda a,b:lambda c,d:lambda e,f:a+b-c*d/e**f


# In[100]:


ab(1,2)


# In[101]:


ab(1,2)(3,4)(5,6)


# In[102]:


ab=lambda x,y:return x+y


# In[116]:


ab=lambda a,b: print(a,"is greater than",b) if a>b else print(b,"greater than",a)


# In[118]:


ab(58,64)


# In[110]:


# even_odd by lambda function:-


# In[111]:


even_odd=lambda x:print(x,"is even.") if x%2==0 else print(x,"is odd.")


# In[112]:


even_odd(58)


# In[132]:


ab=lambda x,y:{"add":x+y,"sub":x-y,"mul":x*y}


# In[133]:


ab(23,5)


# In[137]:


for i,j in ab(2,3).items():
    print(i,"-->",j)


# # Fibonacci Series By Function :- 

# In[1]:


# By for loop:-


# In[3]:


def fibo(n):
    a=0
    b=1
    c=0
    for i in range(n):
        print(c)
        a=b
        b=c
        c=a+b


# In[4]:


fibo(8)


# In[5]:


# By while loop:-


# In[16]:


def fibo(n):
    a=0
    b=1
    c=0
    i=1
    while i<=n:
        print(c,end=" ")
        a=b
        b=c
        c=a+b
        i+=1


# In[20]:


fibo(8)


# In[ ]:





# In[ ]:





# In[ ]:




