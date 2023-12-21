def LargestSquare(n):
 p = 1
 while n >= p*p:
 p += 1
 q = (p-1)*(p-1)
 print("The largest square number is " + str(q))