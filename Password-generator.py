import random

Pass_list =  [list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),list("abcdefghijklmnopqrstuvwxyz"),list("0123456789"),list("!@#$%^&*()_+-={}:;<>?,./'[]|")," "]

Pass = []
n = int(input("Enter a number : "))

'''
for i in range(int(n/4)):
    for j in Pass_list:
        Pass.append(random.choice(j))
print("".join(Pass))
'''

for i in range(n):
        x = i % len(Pass_list)         
        Pass.append(random.choice(Pass_list[x]))

print("".join(Pass))
