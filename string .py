age = 21
print(type(age))
year = str(age)
print(type(year))

password = 'dilesh123'
if len(password)>8:
    print('valid')
else:
    print('invalid')
    
student_grades = {'ram':'C', 'shyam':'A+', 'hari':'B', 'sita':'A+'}
result=list(student_grades.values()).count('A+')
print(result)

# replace method
fruit_name='orange'
print(fruit_name.count('o'))
result=fruit_name.replace('or','A')
print(result)
result1=fruit_name.maketrans('o','A')
print(fruit_name.translate(result1))
print(ord('A')) # A=65 Z=90
print(ord('a')) # a=97 z=122

list=['ram','shyam','gita']
print(list)
# append
list[0]='hari'
print(list)

# strip
name='    laxman kc    '
print(name.strip())

# split method
name='    laxman kc    '
step1=name.split()
print(step1)
print(''.join(step1))

# reverse sentence
userInput = "I love south indian movies"
step1 = userInput.title()
print(step1)
step2=step1.split()
print(' '.join(step2[::-1]))

fullName = input("enter the username: ")
clean = fullName.lower() 
step2= clean.replace(' ','_')
print(f'your username is {step2}')

password = input("enter the password: ")
step1=password.maketrans('aeios','@3!0$')
print(f'your secret code is: {password.translate(step1)}0##9')

fullEmail='laxman.kc@gmail.com'
step1=fullEmail[:9]
print(step1)
step2= step1.replace('.','')
print(step2)

fullEmail='laxman.kc@gmail.com'
step1=fullEmail[:fullEmail.find('@')]
step2=step1.replace('.','')
print(step2)

fullEmail='laxman.kc@gmail.com'
step1=fullEmail.replace('.','')
step2=step1.replace('@gmailcom','')
print(step2)

phone_number= "+977 9849-241-223"
step1=phone_number.replace('-','').replace(',','').replace(' ','')
print(step1)

phone_number="+977 9849-241-223"
clean=phone_number.replace('-','')
print(clean)
