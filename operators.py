def login():
    """login syndicate"""
    print('hello world')
login()
print(login.__doc__)

num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))

# Arithmetic Operators
print(num1+num2)   # addition
print(num1-num1)   # subtraction
print(num1*num2)   # multiplication
print(num1**num2)  # power
print(num1/num2)   # divide
print(num1//num2)  # floor divide(remove decimal)
print(num1%num2)   # modulus(remainder)

# Comparison Operator
print(num1==num2)  # equal to
print(num1!=num2)  # not equal to
print(num1<num2)   # greater than
print(num1>num2)   # less than
print(num1<=num2)  # greater or equal to 
print(num1>=num2)  # less or equal to

# Membership Operator
student_name=['ram','shyam','hari']
print('ram' in student_name) # true
print ('sita' in student_name) #false
print('shyam' not in student_name) #false

number=[1,2,3,4,5]
print(1 in number) # true
print(6 not in number) # true

fruit=['apple','banana','coconot','mango']
name=input('enter a fruit name: ')
if name in fruit:
    print('true')
else:
    print('false')

# Bitwise Operator
print(5&3)  # 0101 (5)
            # 0011 (3)
            # -----
            # 0001 = 1(in decimal)

print(5|3)  # 0101 (5)
            # 0011 (3)
            # -----
            # 0111 = 7(in decimal)

print(~5)   #5=0101,  ~5=1010
            #~x = -(x+1), ~5 = -(5+1) = -6

print(12>>2)  # 12=1100. So, 12>>2(left shift 2 bits)-->11=3

print(12<<2)  # 12=1100. So, 12>>2(right shift 2 bits)-->110000=48

print(5^3)  # 0101 (5)
            # 0011 (3)
            # ----
            # 0110  = 6(in decimal)
