import sys

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def debug(): #no-method-argument
        print 'debug method!'

def add(x, y, z):
    return x + y + z

def subtract(x, x, z): #duplicate-argument-name
    return x + x + z

def main():
    try:
        a = 1
        b = 2

        print add(a, b)      # no-value-for-parameter
        print add(a, b, c)   # undefined-variable
    except Exception:        # bad-except-order
        print 'Exception'
    except LookupError:
        print 'LookupError'

if __name__ == '__main__':
    main()
