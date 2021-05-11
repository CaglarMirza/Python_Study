"""
genious = ("Bill", "Rossum", "Guido Van", "Gates")
# For me, Bill Gates and Guido van Rossum are geniuses.
def merger(par1, par2, par3, par4):
    print(f"For me, {par1} {par4} and {par3} {par2} are geniuses")
merger(*genious)
"""


"""
def gene(x, y):  # defined by positional args
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")


dict_gene = {'y': "Marry", 'x': "Fred"}
gene(**dict_gene)  # we call the function by a single argument(variable)
"""



"""
def gene(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
# iki önemli nokta. Item sayısı ve key isimleri
dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene)  # Dictionary key ve valueları gelir
gene()  # default argümanları getirir
"""


"""
# [("mary", "rye"), ("bella", "fred"), ("linda", "roland")]
dict_couple = {"bride": ["mary", "bella", "linda"],
               "groom": ["rye", "fred", "roland"]}

def couples(bride, groom):
    couple_list = []
    for i in zip(bride, groom):
        couple_list.append(i)
    return couple_list

print(couples(**dict_couple))
"""

"""
dict_couple = {"bride": ["mary", "bella", "linda"],
               "groom": ["rye", "fred", "roland"]}

def couples(bride, groom):
    return [x for x in zip(bride, groom)]
print(couples(**dict_couple))
"""

"""
dict_couple = {"bride": ["mary", "bella", "linda"],
               "groom": ["rye", "fred", "roland"]}
def couples(bride,groom):
    return list(zip(bride, groom))
married = couples(**dict_couple)
print("married = {}".format(married))
"""

"""
friends = {"AhmEt" : 44, "JOSePH" : 39, "LiNDa" : 55, "emir" : 65}
def meaner(AhmEt, JOSePH, LiNDa, emir):
    average = (AhmEt + JOSePH + LiNDa + emir) / len(friends)
    print("The average of their ages is :", average)
(meaner(**friends))
"""

"""
open_list = ["[","{","("]
close_list = ["]","}",")"]
# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
# Driver code
string = "{[]{()}}"
print(string, "-", check(string))
"""

"""
def is_valid(s):
    characters = {'(':')','[':']','{':'}'}
    stack = []
    for i in s :
        if i in characters.keys() :
            stack.append(i)
        elif stack and i == characters[stack[-1]] :
            stack.pop()
        else :
            return False
    return not stack
print(is_valid("}"))
"""

"""
a = input('enter ')
list_a = list(a)
bool_value = False
list_a.insert(0,'sdf')
dict_a = {'(' : ')', '{' : '}', '[' : ']'}
for key,value in dict_a.items():
  for i in range(len(list_a)):
    if list_a[i] == key and list_a[-i] == value:
      bool_value = True
    elif list_a[i] == key and list_a[i +1] == value:
      bool_value = True
print(bool_value)
"""

"""
a=input("Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`:")
b=[]
c=("{[()]}")
for i in a:
    if i in c:
        b.append(i)
x="".join(b)
left=set("{[(")
dict={"(" : ")", "[" : "]", "{" : "}"}
stack=[]
print(x)
for i in x:
    if i in left:
        stack.append(i)
    elif stack and i == dict[stack[-1]]:
            stack.pop()
    else:
        print(False)
if stack==[]:
    print(True)
"""

"""
string=input("Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`:")
while ("()" in string) or( "[]" in string)  or ("{}" in string) :
    string=string.replace("()","")
    string=string.replace("[]","")
    string=string.replace("{}","")
if len (string)== 0:
    print(True)
else:
    print(False)
"""

"""
def query(s):
    while "()" in s or "{}" in s or '[]' in s:
        s = s.replace("()", "").replace('{}', "").replace('[]', "")
    return s == ''
x = "()[]()[]"
print(query(x))
"""

"""
def square(x):
    return x**2
# lambda x: x**2
"""

"""
print((lambda x, y: (x+y)/2)(3, 5))  # takes two int, returns mean of them
"""

"""
tek_cift = lambda x: 'tek' if x % 2 else 'cift'
print(tek_cift(55))
"""

"""print((lambda x: 'tek' if x % 2 else 'cift')(6))"""

"""print((lambda x, y: (x+y)/2)(3, 5))  # takes two int, returns mean of them"""

"""average = (lambda x, y: (x+y)/2) (3, 5)
print(average)"""

"""iterable = "clarusway"
reverser = print((lambda x : x[::-1]) (iterable))"""


"""a = [1,2,3,4]
for i in a:
    print(i," : ", (lambda x : "odd" if not x%2 else "even" )(i))"""

"""hipotanüs = lambda a, b : a**2 + b**2
print(hipotanüs(2, 3))"""

"""iterable = "clarusway"
reverser = (lambda x : x[::-1])
print(reverser(iterable))"""

"""
iterable = [1, 2, 3, 4, 5]
map(lambda x:x**2, iterable)
result = map(lambda x:x**2, iterable)
print(type(result))  # it's a map type

print(list(result))  # we've converted it to list type to print

print(list(map(lambda x:x**2, iterable)))  # you can print directly
"""

"""
iterable = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 2, iterable)
# print(type(result))
# print(result)
# print(*result)
# print(list(result))
# print(list(map(lambda x:x**2, iterable)))
"""

"""
iterable = ["ahmet", "abdurrahman", "nereye geldik?"]
print(list(map(len, iterable)))
"""

"""
letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']
numbers = map(lambda x, y, z: x+y+z, letter1, letter2, letter3)

print(list(numbers))
"""

"""
list1 = ["a", "b", "c"]
list2 = ["x", "y", "z"]
yapıştır = map(zip, list1,list2)
for i in yapıştır:
    for j in i:
        print(j)
"""

list1 = ["a", "b", "c"]
list2 = ["x", "y", "z"]
yapıştır = map(zip, list1,list2)


