import sys
p = True
num = int(sys.argv[1])
for item in range(2,num-1):
 print(item)
 if (num%item) == 0:
  p = False
#   print ("num is not a prime")
  break
 else:
  continue

if (p == True):
  print (" num is prime")

else:
  print(" num is not a prime")
