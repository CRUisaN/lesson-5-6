import colorama
import sys
import inspect

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))
print(inspect.getmodule(colorama))
print(inspect.getmodule(list))

def first_function():
    pass

class Human:
    pass

rq=colorama
first_1=first_function
nick=Human

print(colorama.__name__)
print(rq.__name__)
print(first_1.__name__)
print(first_function.__name__)
print(nick.__name__)
print(Human.__name__)
print(__name__)

print(type(1))
print(type(1.6))
print(type(1==1))
print(type("HI"))

intro_dict={}
for method in dir(intro_dict):
    print(method)

for method in dir():
    print(method)

print(sys.executable)
print(sys.version)
print(sys.platform)

for _ in dir(__builtins__):
    print (_)