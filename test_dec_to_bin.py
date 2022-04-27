# Python3 code to demonstrate 
# decimal to binary number conversion
# using format() + list comprehension

# list for single binary digits
res = [None]

# initializing number 
# test_num = 1
test_num = int(input("Pass only an int value: "))
  
# printing original number
print ("The original number is : " + str(test_num))
  
# using format() + list comprehension
# decimal to binary number conversion 
res = [int(i) for i in list('{0:0b}'.format(test_num))]

# making the array of minimal expected length (adjusting to the number of LEDs to light: 4 for hours, 5 for minutes)
while len(res) < 4:
    res = [0] + res

# printing result 
print ("The converted binary list is : " +  str(res))

# printing the single items of the array
for x in range(len(res)):
    print(("Place ") + str(x) + ": " + str(res[x]))

# printing the last bit (check the number if even or odd )
print("Last bit: " + str(res[-1]))