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
# def almost_there(n):
#     return abs(100 - n) <= 10 or abs(200 - n) <= 10

# Find 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# def has_33(nums):
#     for i in range(0, len(nums)-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# def paper_doll(text):
#     new_word = ''
#     for letter in text:
#         new_word += letter * 3
#     return new_word


#### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# def blackjack(a, b, c):
#     if a + b + c <= 21:
#         return a + b + c
#     elif (a+b+c) > 21 and (a == 11 or b == 11 or c == 11):
#         return a+b+c - 10
#     else:
#         return 'BUST'

#### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# def summer_69(arr):
#     total_count = 0
#     add = True

#     for num in arr:
#         while add:
#             if num != 6:
#                 total_count += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total_count


#### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# def spy_game(nums):

#     checklist = [0, 0, 7, 'Secret Code']
# #     [0,7, 'Encrypted Code'] (expected array after popping out the first item in the list equaling zero)
# #     [7,'Encrypted Code'] (expected array after popping out the second item in the list equaling zero)
# #     ['Encrypted Code'] (expected array after popping out the third item in the list equaling seven)
# #     putting a random value that it cannot hit allows the code to be evaluated with the length of one, Have to look into the underlying reason why comparing it with the value of zero does not allow the code to exicute
#     for num in nums:
#         if num == checklist[0]:
#             checklist.pop(0)
# #   if the length is equal to zero, 007 is in the list
#     return len(checklist) == 1


#### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
# def count_primes(num):
#     #     check for zero or one
#     if num < 2:
#         return 0
# #     case for two or greater

# # stored prime numbers
#     primes = [2]

# # counter going up to the input number
#     counter = 3
#     while counter <= num:
#         #         checking if x is prime
#         for y in range(3, counter, 2):
#             if counter % y == 0:
#                 counter += 2
#                 break
#         else:
#             #     python allows you to do for else statements since you have a break in the previous line
#             primes.append(counter)
#             counter += 2
#     print(primes)
#     return len(primes)

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
# class Line:

#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2

#     def distance(self):
#         return ((self.coor1[1] - self.coor2[1]) ** 2 + (self.coor1[0] - self.coor2[0])**2)**.5

#     def slope(self):
#         return ((self.coor2[1] - self.coor1[1])/((self.coor2[0] - self.coor1[0])))
# 



# calculations for a cylinder 
# class Cylinder:

#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return 3.14 * self.radius**2 * self.height

#     def surface_area(self):
#         return 2 * 3.14 * self.radius * self.height + 2 * 3.14 * self.radius**2


# create a bank account class that has two attributes Owner and balance
# and two methods: deposit and withdraw
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f" added {amount} to balance")

    def withdraw(self, take):
        if take > self.balance:
            return print('Dunds Unavaliable')
        else:
            self.balance = self.balance - take
            return print('Withdrawal Accepted')

    def __str__(self):
        return f"Owner: {self.owner} \n Balance: {self.balance}"
