# l1 = ['a', 'b', 'c']
# l2 = ['m', 'n', 'o']
# l1.append('p')
# l2.extend(l1)
# l2.sort(reverse=True)
# l2.remove('m')
# print(l2)

# tuple2 = ("banana", "cherry")
# tuple1 = ("apple",)

# tuple2+=tuple1
# print(tuple2)

# myset = {"apple", "banana", "cherry"}
# # Order is not predictable here as it is based on some hash algo used to store set efficiently
# myset.add("orange")
# mylist = ["kiwi", "orange"]
# myset.update(mylist)
# myset.remove("orange")
# print(myset)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.keys())

# for x, y in thisdict.items():
#   print(x, y)

from queue import PriorityQueue
pq = PriorityQueue()
for i in range(3):
    temp = 3-i
    pq.put(temp)
print("Elements in PriorityQueue:")
while not pq.empty():
    print(pq.get())


# from collections import defaultdict
# my_dict = defaultdict(str)
# my_dict['fruits'] = 'apple'
# my_dict['vegetables'] = 'carrot'
# print(my_dict.items())
# for x, y in my_dict.items():
#     print(x,y)


# import json
# # Below is json string
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(type(y))
# print(json.dumps(y))
# print(type(json.dumps(y)))



vara = 123
print(f"variable a = {vara}")



# nested obj is changes in copy while it will not change in case of deepcopy
import copy
templst = [[1],2,3]
newlst = copy.copy(templst)
newlst[0][0] = 4
print(templst)
print(newlst)
newlst2 = copy.deepcopy(templst)
newlst2[0][0] = 6
print(templst)
print(newlst2)


testset = set(['a', 'b', 'a'])
testset.add('r')
for x in testset:
  print(x)


from collections import deque
dq = deque()
dq.append(1)
dq.append(10)
dq.appendleft(4)
dq.append(5)
while len(dq) > 0:
  print(dq.pop())


# import heapq
# li = []
# for i in range(3):
#     temp = int(input("Enter element into heap: "))
#     heapq.heappush(li, temp)

# while li:
#     print(li[0])
#     heapq.heappop(li)


from collections import OrderedDict
numbers = OrderedDict(one=1, two=2, three=3)
# numbers = dict(one=1, two=2, three=3)
numbers.move_to_end("one")
numbers.popitem()
for key in reversed(numbers):
  print(key, "->", numbers[key])

# named tuples
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])

p1 = Person("Alice", 30, "New York")
p2 = Person("Bob", 25, "Los Angeles")

print(p1.name)
print(p2.age)
print(p1[2])


# dict comprehension
tempdict = {x: x**2 for x in range(10)}
print(tempdict)

#generators
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Returns count and pauses
        print("here")
        count += 1   # Resumes from here

gen = count_up_to(5)
for x in gen:
  print(x)
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2

squares = (x**2 for x in range(1000000))
print(squares)
print(next(squares))
print(next(squares))


# class methods
class Car:
  count = 0

  def __init__(self, brand):
    self.brand = brand
    Car.count += 1

  @classmethod
  def get_count(cls):
    return f"Total cars: {cls.count}"

car1 = Car("Tesla")
car2 = Car("BMW")

print(Car.get_count())  # ✅ Accessing class attribute


# positional vs keyword args
def checkf1(p1, p2, p3):
  print(p1)
  print(p2)
  print(p3)
  print("checkf1")

checkf1("p1", p3="da", p2="das")

# data classes
from dataclasses import dataclass

@dataclass
class Person:
  name: str
  age: int = 30

p1 = Person("Alice")
print(p1)

# private attributes and methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # private variable (name mangled)
 
  def __str__(self):
    return f"{self.name}({self.__age})"  

  def get_age(self):
    return self.__age

  def __greet(self): # private method (name mangled)
    return f"Hello, {self.name}!"

  def public_method(self):
    return self.__greet() # Calling private method inside the class

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

p1 = Person("John", 36)
print(p1.name)
# print(p1.__age) # ❌ Person object has no attribute __age
print(p1.get_age()) 
print(p1._Person__age)
# print(p1.__greet())  # ❌ AttributeError: MyClass object has no attribute __greet
print(p1._Person__greet())  # ✅ Works, but not recommended
print(p1.public_method())

class EvenNumbers:
  n = 2
  def __iter__(self):
    return self

  def __next__(self):
    x = self.n
    self.n += 2
    return x

even = EvenNumbers()
it = iter(even)
print(next(it))
print(next(it))


testvar = "hello123"
temp = iter(testvar)
print(next(temp))
print(next(temp))

# Decorators
def testfunc(func):
  def test2():
    print("before")
    func()
    print("after")
  return test2

@testfunc
def tempgreet():
  print("hello")

tempgreet()

