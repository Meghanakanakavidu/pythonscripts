#q: 1 2 3 4 5 6 7 8 9 10

a = [1,2,3,4,5,6,7,8,9,10]
b = [3,4,5,6,7,8]
c = b[::-1]
x = a[0:2] + c + a[-2:]
print(x)
a.insert(5,23)
print (a)
y = [1,2,9,10]

for item in b:
  y.insert(2,item)
print(y)

