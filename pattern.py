# star pattern
n=int(input("Enter the number: ")) 
for i in range(1, n+1):
    print(" " * (n-i),end="")
    print("*" *(2*i-1))


# searching  a number 

tuple=(1,4,9,16,25,36,49,64,81,100)
x=16
index=0
for i in tuple:
    if (i==x):
      print(" number found at index", index)
      break
    index+=1


# print elements

list=[1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)


