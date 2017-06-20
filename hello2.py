"""This module prints hello"""

class HelloWorld:
    """This class prints out hello world"""
    def __init__(self):
        """Main method contains nothing"""
        pass

def method1(n):
    """This is the first method"""
    one, two = 0, 1
    while two < n:
        print(two)
        one, two = two, one+two

print("Hello, World")

hello = HelloWorld()
method1(500)
name = input()
print(name)
