#prime numbers 
l1=[]
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        l1.append(Number)

#fibanocci series 
l=[]
n1, n2 = 1, 2
count = 0
if 100 <= 0:
   print(" ")
elif 100 == 1:
   l.append(n1)
else:
   while count < 100:
      l.append(n1)
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
#merging prime and fibanocci lists 
z=list(zip(l,l1))
b=[]
for i in z:
   b.append(list(i))
m=[]
for i in b:
   for j in i:
      m.append(j)
t=int(input())
arr=list(map(int,input().split()))
for i in arr:
    print(m[i-1],end=" ")
