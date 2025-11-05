'''try:
    num=int(input("enter number:"))
    print(f"you entered:{num}")
except ValueError:
    print("thats not valid number! please enter integer")
print("program continues after the try-except block")
#
try:
    x=10/0
except ZeroDivisionError:
    print("cannot divide by zero")'''
#
try:
    num=int(input("enter number:"))
    print(10/num)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input")
else:
    print("no exceptions occured")
finally:
    print("execution complete")
