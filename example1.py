import sys

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def debug():
        print 'debug method!'

def add(x, y, z):
    return x + y + z

def subtract(x, x, z):
    return x + x + z

def main():
    try:
        a = 1
        b = 2

        print add(a, b)
        print add(a, b, c)
    except Exception:
        print 'Exception'
    except LookupError:
        print 'LookupError'

if __name__ == '__main__':
    main()
