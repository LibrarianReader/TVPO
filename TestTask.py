import unittest

def maxsort(f,l):
    list = f
    if l==max(list, key=len):
        return True
    else:
        return False

def minsort(f,l):
    list = f
    if l==min(list, key=len):
        return True
    else:
        return False

if __name__ == '__main__':
    print(maxsort(["Gon","Li"],"Gon"))
    print(minsort(["Gon","Li"],"Li"))