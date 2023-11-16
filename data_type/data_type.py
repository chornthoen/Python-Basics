import math
num = 20
name = 'python'
bool = True
f = 10.5

print(type(num))
print(type(name))
print(type(bool))

last = 'chorn'
first = 'thoen'
age = 20
say = 'hey! how are you?'
fullname = last + ' ' + first
print("String data type".center(40, '=').title())
print(fullname)
print('My name is ' + fullname + ' and I am ' + str(age) + ' years old.')
print('My name is {} and I am {} years old.'.format(fullname, age))
print('My name is {0} and I am {1} years old.'.format(fullname, age))
print('My name is {1} and I am {0} years old.'.format(age, fullname))
print(f'My name is {fullname} and I am {age} years old.')

print(fullname.upper())
print(fullname.lower())
print(fullname.capitalize())
print(fullname.title())
print(fullname.swapcase())
print(fullname.replace('chorn', 'Chorn'))
print(fullname.find('chorn'))
print(fullname.find('thoen'))
print(len(fullname))
print('chorn' in fullname)
print('chorn' not in fullname)


print(say.split(" "))
print(say.split(' ')[0].upper())
print(say.title())

title = 'Programming language'.upper()
j = 'java programming'.title()
c = 'c programming'.title()
cs = 'c# programming'.title()
js = 'javascript programming'.title()
print(title.center(40, '='))
print(j.ljust(30, '.') + "30$".rjust(10))
print(c.ljust(30, '.') + "30$".rjust(10))
print(cs.ljust(30, '.') + "30$".rjust(10))
print(js.ljust(30, '.') + "30$".rjust(10))

# boolean data type
print()
print("Boolean data type".center(40, '=').title())
print(bool)
print(type(bool))
print(bool is True)
print(bool is False)
print(bool is None)
print(bool is not None)
print(bool == True)

# integer data type
print('Integer data type'.center(40, '=').title())
print(num)
print(type(num))
print(num + 10)
print(num - 10)
print(num * 10)
print(num / 10)
print(num // 10)
print(num % 10)
print(num ** 10)

# float data type
print('Float data type'.center(40, '=').title())
print(f)
print(type(f))
print(f + 10)
print(f - 10)
print(f * 10)
print(f / 10)
print(f // 10)
print(f % 10)
print(f ** 10)

# complex data type
print('Complex data type'.center(40, '=').title())
c = 1 + 2j
print(c)
print(type(c))
print(c.real)
print(c.imag)
print(c.conjugate())

# Built-in functions for numbers
print('Built-in functions for numbers'.center(40, '=').title())
print(abs(-10))
print(abs(10))
print(round(10.5))
print(round(10.4))
print(round(10.6))

# math
print('Math'.center(40, '=').title())
print(math.ceil(10.1))
print(math.floor(10.9))
print(math.sqrt(100))
print(math.pow(10, 2))
print(math.pi)
print(math.e)
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))


