# two.py
# testing our order of code that runs

import one
print('top level in two.py')

one.func()


# handels the errors when changing between file names
if __name__ == "__main__":
    print('two.py is run directly ')
else:
    print('two.py has been imported')
