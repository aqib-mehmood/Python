
# Task 01 
# Write a program that prints triangle using loops in python.
print("----------- Task 01 Solution -----------")
for triangle in range(10):
    print("*" *triangle)
  
  

# Task 02
# Write a program that prints Fibonacci series.
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34.....
# 0 1 1 2 3 4 5 
'''
print("----------- Task 02 Solution -----------")
n1 = 0 
n2 = 1
print(n1)
print(n2)
for var in range(10):
    result = n1+n2
    n1 = n2
    print(result)
    n2 = result
    '''

  
    

# Task 03
# Write a short program that prints each number from 1 to 100 on a new line. 
#       For each multiple of 3, print “SAM" instead of the number. 
#       For each multiple of 5, print “SUNG" instead of the number
#       For numbers which are multiples of both 3 and 5, print “SAMSUNG" instead of the number.

'''
print("----------- Task 03 Solution -----------")

for number in range(16):
    #print(number+1)
    if ((number % 3 == 0) and (number % 5 == 0)):
        print("SAMSUNG")
    elif (number % 3 == 0):
        print("SAM")
    elif (number % 5 == 0):
        print("SUNG")
    else:
        pass
    '''
