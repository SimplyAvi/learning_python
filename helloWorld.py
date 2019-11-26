print('hello world from pythons code in terminal')
# ran python within terminal - python helloWorld.py

print('can i see this on github?')

print('whats going on here?')


print('for comments to go through you need to get add .')
print('then you git commit -m "what ever message" ')
print('then git push')

print('have to work on git merge to check the differences between one branch on git to the other so that it doesnt over ride the wrong thing')

# Methonds and functions

# first funtion written in python
# def myfunc():
#     print('hello world')

# first funtion with an input and string interpulation
# def myfunc(name):
#     print('Hello {}'.format(name))

#  first function with an argument and conditional statment
# def myfunc(arg):
#     if arg == True:
#         return "hello"
#     elif alse:
#         return 'goodbye'

# using multiple inputs to check boolean statements

# def myfunc(x, y, z):
#     if z == True:
#         return x
#     elif z == False:
#         return y

# doing simple math with functions


# def myfunc(arg1, arg2):
#     return arg1 + arg2

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        #         both numbers are even
        if a < b:
            result = a
        else:
            result = b
#             you can return min(a,b)
    else:
        #     numbers are odd
        if a < b:
            result = b
        else:
            result = a
#             you can return max(a,b)
    return result
