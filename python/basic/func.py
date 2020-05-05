print("hello")

def greet(username='jhon'):
    print("hello, " + username.title())

greet('dayu')
greet()
greet(username='lee')

print("-----------------------------------------------------")

def pet(name, desc='beautiful'):
    print(name.title() + " is so " + desc)

pet('dog', 'cute')
pet(name='the building', desc='so hight')

print("-----------------------------------------------------")

def build_upper(desc):
    return desc.upper()

cat = build_upper('cat')
pet(cat)

print("-----------------------------------------------------")

def build_dict(first, last, age=''):
    if age:
        age = int(age) * 2
    new_dict = {'first' : first, 'last' : last, 'age' : age}
    return new_dict
dict = build_dict('yu', 'da', 12)
print(dict)

print("-----------------------------------------------------")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
complated_modes = []

all = unprinted_designs[:]
while all:
    current_design = all.pop()
    complated_modes.append(current_design)

for mode in complated_modes:
    print(mode)

print(all)
print(unprinted_designs)

print("-----------------------------------------------------")

def make(*things):
    print(things)

make('fdf', 'fd', 'dfd')


def desc(name, desc='beautiful'):
    assmeble = name.title() + " is so " + desc
    return assmeble