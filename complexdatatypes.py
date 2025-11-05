Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=3+5j
>>> print(a)
(3+5j)
>>> a=0B11+5j
>>> print(a)
(3+5j)
>>> a=3+0B11j
SyntaxError: invalid binary literal
>>> c=10.5+3.6j
>>> print(c)
(10.5+3.6j)
>>> print(c.real)
10.5
>>> print(c.imag)
3.6
