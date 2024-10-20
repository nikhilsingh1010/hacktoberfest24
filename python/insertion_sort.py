l = eval(input("enter a list"))
k = len(l)
for i in range(k):
    temp = l[i]
    ptr = i-1
    while l[ptr]>temp and ptr >= 0:
        l[ptr+1] = l[ptr]
        ptr = ptr-1
    l[ptr+1] = temp
print(l)
