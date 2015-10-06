import sys

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def debug(): #Method has no argument
        print 'debug method!'

def add(x, y, z):
    return x + y + z

def subtract(x, x, z): #Duplicate argument name
    return x + x + z

def main():
    try:
        a = 1
        b = 2

        print add(a, b)      # No value for argument z
        print add(a, b, c)   # Undefined variable c
    except Exception:        # Bad exception clauses
        print 'Exception'
    except LookupError:
        print 'LookupError'

if __name__ == '__main__':
    main()
