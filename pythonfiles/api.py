import socket
age = 23
age_str = "23"
price = 45.09
name = "gabriel"
items = []
objects = {}
tripple = ()
int()
float()
str()
list()
tuple()
set()
dict()


try:
    print(age+ int(age_str))
except TypeError as e:
    print("an error occured ", e)
except SyntaxError as e:
    print("an error occured ", e)
else:
    print("successfully executed")
finally:
    print("code finish line")

# print(age)
print(socket.gethostbyname("www.bsum.edu.ng"))