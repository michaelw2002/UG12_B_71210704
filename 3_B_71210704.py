word1 = str(input("Input :"))
length = len(word1)
print("Output :")
for i in range(length):
    for j in range(length-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(word1[j],end=" ")
    print()
for i in range(length):
    for j in range(i):
        print(" ",end=" ")
    for j in range(length-i):
        print(word1[j],end=" ")
    print()
