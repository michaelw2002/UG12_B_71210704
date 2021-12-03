n = int(input("Masukkan banyak bilangan : "))
i = 1
print("Total = ",end="")
for a in range(1,n+1):
    if a%7==0:
        i=i+0
        print('+ 0',end=' ')
    elif a%3==0:
        i=i+(a * -1)
        print("- "+str(a),end=' ')
    elif a==1:
        print(str(a),end=" ")
    else:
        i=i+a
        print ('+ '+str(a),end=' ')
print("\nHasil perhitungan diatas ialah "+str(i))
