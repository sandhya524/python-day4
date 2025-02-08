# # num1 = 10
# # num2 = 20
# print(num1 + num2)
# print(num1 - num2)
# print(num1 / num2)
# print(num1 * num2)
# print(num1 // num2)#floor division
# print(num1 % num2)#exponent
# print(num1 ** num2)

#bodmas rule

# print( 1 - 3 * 5)
# print( (1 -3 ** 2) * 5)

# #assignment operators

# # num1 = 5
# # print(num1 + 5)
# # print(num1)

# # num1 = num1 + 5
# # print(num1)

num1 = 5
num1 += 5
print(num1)
num1 -= 3
num1 *= 4

#relational opearators
print(3 > 5)
print(3 >= 5)
print(3 == 5)
print(3 <= 5)
print(3 != 5)
print(3 < 5)

#logical operators
print(True and True)
print(3 > 5 and 2 < 3)
print(False and (True and False and True))
print( 2 and 3)
print(3 and 2)
print(0 and 2)
print(2 and 0)
print("" and True)
print(1 and [])
print(-1 and -2)
print(-3 and -2)

#or
print(True or True)
print(3 > 5 or 2 < 3)
print(False or (True and False and True))
print( 2 or 3)
print(3 or 2)
print(0 or 2)
print(2 or 0)
print("" or True)
print(1 or [])
print(-1 or -2)
print(-3 or -2)

#not operator
print(not True)


#bitwise
print(11 & 14)# and operation
print(bin(11))
print(bin(15))
print(12 & 23)

#|
print(9 | 11)
print(16 | 20)
print(3 | 12)



#^
print(13 ^ 11)
print(9 ^ 11)
print(bin(139))
print(type(139))

#Leftshift Operation
print(27 << 1)
#Binary value of 27 is 11011 and it moves one position left so the 110110 
#the value of 110110 is 54
print(16 << 4)
#here 16 moves 4 times to left position so we can multiply the value with 2 for four times
#16*2=32
#32*2=64
#64*2=128
#128*2=256

print(8 << 2)
#here 8 moves 2steps towards left so multify the number with 2 for two times
#8*2=16
#16*2=32

# print("sandhya" << 2)#unsupported operand types for <<: str and int
#print([1,2,3] << 1) #unsupported operand types for <<: list and int
# print((1,2,3) << 2 ) #unsupported operand types for <<: tuple and int

#Rightshift Operators
print(16 >> 2)#here 16 moves 2 steps towards right so we can divide the number for two times
#16/2=8
#8/2=4
#output is 4
print(35 >> 2)#here 32 shifts 2 positions towards right so the process is
#35/2=17.5
#17.5/2=8.75
#the output shows only integer part like floor division
#output is 8


# print("sandhya" >> 2)#unsupported operand types for <<: str and int
#print([1,2,3] >> 1) #unsupported operand types for <<: list and int
# print((1,2,3) >> 2 ) #unsupported operand types for <<: tuple and int



