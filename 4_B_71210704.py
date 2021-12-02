n = int(input("Input : "))
print("Output :")
for row in range(n):
    for col in range(n):
        if col==(n-1) or row==(n-1) or col+row+1==n: #letak * pada kolom dan baris
            print("*",end="")
        else:
            print(end=" ")
    print()
