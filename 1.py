a=1
b=2
c=a+b
print(c)

if 10==10:
    print("both are equal")

import keyword
print(keyword.kwlist)

import keyword
print(len(keyword.kwlist))

print("what's up")
print('what\'s up')

print("* * * * *")
print("*       *")
print("*       *")
print("*       *")
print("*       *")
print("* * * * *")

print("* * * * *\n*\t*\n*\t*\n*\t*\n*\t*\n* * * * *")

print("*\n**\n***\n****\n*****")

print("           __")
print("          /._)")
print("   .-^^^-/ /")
print("__/       /")
print("<__.|_|-|_|")

print("* * * * * * * * *")
print("  * * * * * * *  ")
print("    * * * * *    ")
print("      * * *      ")
print("        *        ")

print("        *        ")
print("      * * *      ")
print("    * * * * *    ")
print("  * * * * * * *  ")
print("* * * * * * * * *")
print("  * * * * * * *  ")
print("    * * * * *    ")
print("      * * *      ")
print("        *        ")

name = "ram"
print(f"my name is {name}")
print(f"{name} want to be a coder")


domainName = "codewithdurga"
print(f"learn@{domainName}.com")
print(f"support@{domainName}.com")
domainName = "codewithharry"
print(f"www.{domainName}.com")

name = """python 
             programming"""
print(name)

name = 'ram'
last_name = 'kc'
age = 50
# print(f'my name is {name}')
# print(age)
print('my name is {3}'.format(name, last_name, age))

print('my name is {0} {2} and i want to learn {1}'\
      .format('shyam','python','basnet',name='ram',age=50))

items=['apple','milk']
# append extend
print(items)
items.append('sugar')
print(items)


name = 'dIlEsH'
result = name.upper()
print(result)
print(name)

name = 'dIlEsH'
result = name.lower()
print(result)

name= 'ram'
result=name.center(9)
print(result)
# odd left_slide = (n+1)/2 right_side = (n-1)/2
# even left_slide = (n-1)/2 right_side = (n+1)/2
name = "ram"
test = name.center(6, '*')
print(test)

invoice_no = 666
formatted_no = str(invoice_no).zfill(5)
customer = "John Doe"
amount = 199.99 
print('=' * 50)
print('\t\tINVOICE')
print(f'\tInvoice No: INV-{formatted_no}')
print(f'\tCustomer: {customer}')
print(f'\tAmount: ${amount}')
print('=' * 50)

print('=' * 40)
invoice_no = 1
customer_name = 'ram'
amount = 12
print("INVOICE".center(35))
print(f'\tInvoice No: INV-{str (invoice_no).rjust(5,'0')}'.center(35))
print(f'\tCustomer: {customer_name.title()}'.center(28))
print(f'\tAmount: ${amount}'.center(18))
print('=' * 40)

name='python'
print(name[7:2])
print(name[-9:2:])
print(name[-3:4:])

a='Expression'
print(a[::2])
print(a[:])
print(a[-2:3:-1])
print(a[-3:4])
print(a[-3:-4:-1])
print(a[-3:7:-2])
print(a[1:-8])
print(a[9::-10])
print(a[9:-10:-1])
print(a[11::-6])
print(a[2:-15:-1])
print(a[-15::-2])
print(a[7:-1])
print(a[-1:0:])
print(a[:-1:])
print(a[::-1])
print(a[-1:7])
print(a[:-3:])
print(a[-1:0])
programming_language = 'python programming'
print(programming_language[6])
print(programming_language[-12])
print(programming_language[0])
print(programming_language[-1])
print(programming_language[9])
print(programming_language[::1])
print(programming_language[::-1])
print(programming_language[7:])
print(programming_language[:6])
print(programming_language[-11:]) 
print(programming_language[0:18:2])
print(programming_language[1:18:3])
print(programming_language[-18::4])
print(programming_language[::5])
print(programming_language[::-3])
print(programming_language[2:15])
print(programming_language[-16:-3])
print(programming_language[7:18])
print(programming_language[:10:-1])
print(programming_language[-1:-10:-2])
print(programming_language[::2])
print(programming_language[1::2])
print(programming_language[3:18:4])
print(programming_language[-15:18:3])
print(programming_language[-1::-1])
print(programming_language[0:6])
print(programming_language[7:18])
print(programming_language[-18:-12])
print(programming_language[-11:])
print(programming_language[6:7])
print(programming_language[:])
print(programming_language[::])
print(programming_language[0:18:1])
print(programming_language[-18:18])
print(programming_language[5:-5])
print(programming_language[-10:-1])
print(programming_language[-1:-19:-1])
print(programming_language[17::-1])
print(programming_language[:0:-1])
print(programming_language[10:0:-2])
print(programming_language[0:18:3])
print(programming_language[1:18:4])
print(programming_language[-17:-1:2])
print(programming_language[-18:0:2])
print(programming_language[::7])

value = 5
print(f"{value*value}")

a = 10
b = 20
print(f'{10*b}')

name = 'DLesh'
print(f"{name*3}")

fname = 'DLesh'
lname = 'Prajapati'
print(f"{fname + lname}")

