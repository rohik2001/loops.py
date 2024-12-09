'''for i in range(10):
    print(i)
for j in range(1,21):
    print(j)
for k in range(51,100,2):
    print(k)
for l in range(33,22,-1):
    print(l)'''
#200+200+....+200
total = 0
for x in range(200,221):
    total=total+x
print("total= ",total)

vitamin=['vitamin-c','protin','water','nuts']
for a in vitamin:
    print(f'Every day you have to take {a}!')

fruits = ['apple','banana','cherry']
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
#nested loop
#outer lopps for rows
for i in range(1,4):
    for j in range(1,4): #inner for collum
        print(f"{i} X {j}  = {i*j}")
    print()

#find prime num
for num in range(2,101):
    is_prime= True
    for divison in range(2,num):
        if num%divison==0:
            is_prime=False
            break
    if is_prime:
        print(f"{num} is a prime number")