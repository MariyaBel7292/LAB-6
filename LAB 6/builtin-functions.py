#builtin-functions
#1
my_list = list(map(int, input().split()))
product = 1
for i in range(len(my_list)):
    product *= my_list[i]
print(product)

#2
s = input()
upper, lower = 0, 0
for i in range(len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        upper += 1
    elif ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
        lower += 1
print("number of upper case letters:", upper, "\nnumber of lower case letters:", lower)

#3
s = input()
a = reversed(s)
r = "".join(a)
print("YES") if s == r else print("NO")

#4
import time
number = int(input("Sample Input:\n"))
milliseconds = int(input())
root = pow(number, 0.5) 
print("Sample Output:")
time.sleep(milliseconds / 1000)
print("Square root of", number, "after", milliseconds, "is", root)

#5
my_tuple = ("Astana", "Almaty", "Mektep", True, False, 0, 4, 7)
print(all(my_tuple))
