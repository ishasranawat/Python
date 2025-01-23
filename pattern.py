# star pattern
n=int(input("Enter the number: ")) 
for i in range(1, n+1):
    print(" " * (n-i),end="")
    print("*" *(2*i-1))


# another method
def pattern(n):
    for i in range(1,n+1):
        spaces= " " *(n-i)
        stars= "*"* (2*i-1)

        print (spaces+stars)

n=int(input())
pattern(n)

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


# print a table using for loop
a=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{a}*{i} = {a*i}") 


#table using while loop
a=int(input("Enter the number: "))
i=1
while(i<=10):
    print(f"{a}*{i} = {a*i}") 
    i+=1






