# one.py
# testing out order of code that runs
# print('hello')


def func():
    print('Func() in ONE.py')

print('top level in one.py')

if __name__ == '__main__':
    # run some function
    print('one.py is being run directly!')
else:
    print('One.py is imported')