a = int(input())
b = int(input())
for i in range(a, b, 2):
    if(i % 2 == 1):
        i+=1
    print(i)