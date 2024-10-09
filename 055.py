def kobeitu_kestesi():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}", end="\t")
        print()

kobeitu_kestesi()


#Lesson
n=int(input("Kai sandy engizu kalaisyz:"))
for a in [1,2,3,4,5,6,7,8,9]:
    for b in [1,2,3,4,5,6,7,8,9]:
        print(f"{a}*{b}=",a * b)
    if a==n:
       break
print()

