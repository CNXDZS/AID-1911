from ctypes import*
from sys import *
from binascii import *
a=23333
print(id(a))
print(hexlify(string_at(10914656,getsizeof(a))))