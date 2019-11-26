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
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         #         both numbers are even
#         if a < b:
#             result = a
#         else:
#             result = b
# #             you can return min(a,b)
#     else:
#         #     numbers are odd
#         if a < b:
#             result = b
#         else:
#             result = a
# #             you can return max(a,b)
#     return result


#### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# def animal_crackers(text):
#     word_arr = text.split()
#     if word_arr[0][0].lower() == word_arr[1][0].lower():
#         return True
#     else:
#         return False

#     you can also run this as a one liner :
#   return word_arr[0][0].lower() == word_arr[1][0].lower()

#### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# def makes_twenty(n1, n2):
#     if n1 + n2 == 20:
#         return True
#     else:
#         return n1 == 20 or n2 == 20

#     also written with or statement
#       return (n1 + n2) == 20 or n1 == 20 or n2 == 20

#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
    # def old_macdonald(name):
    # this is wrong
                            #     new_word = ''
                            #     i = 0
                            #     for letter in range(0, len(name)):
                            #         i += 1
                            #         if i == 1 or i == 5:
                            #             new_word += letter.upper()
                            #         else:
                            #             new_word += letter
                            #             i+=1
                            #     return new_word
# done with the code below
    # first_split = name[:3]
    # remaining_split = name[3:]

    # return first_split.capitalize() + remaining_split.capitalize()

#### MASTER YODA: Given a sentence, return a sentence with the words reversed
# def master_yoda(text):
#     word_arr = text.split()
# #     splits the words to work with them individually
#     result = word_arr[::-1]
# #     reverses the order of the letters inside of the words
#     return ' '.join(result)
# #   returns the array into a string of words seperated by a apsce


#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10
