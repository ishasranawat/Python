# 1.
a= int(input("Enter your score:"))

if(90<=a<=100):
    print("Your grade is .")
elif(80<=a<90):
    print("Your grade is A.")
elif(70<=a<80):
        print("Your grade is B.")
elif(60<=a<70):
     print("Your grade is C.")
elif(50<=a<60):
    print("Your grade is D.")
else:
    print("Your grade is F.")


# 2.
sub1=int(input("Enter the marks of subject1: "))
p1= (sub1/100)*100
sub2=int(input("Enter the marks of subject2: "))
p2= (sub2/100)*100
sub3=int(input("Enter the marks of subject3: "))
p3= (sub3/100)*100


total= sub1+sub2+sub3
percentage=float((total/300)*100)

if(p1>=33 and p2>=33 and p3>=33 and percentage>=40):
   print(f"Your percentage is {percentage:.2f}%,you have passed!") 

else:
  print("You have failed")


# 3.
num1= int(input("Enter num1: "))
num2= int(input("Enter num2: "))
num3= int(input("Enter num3: "))
num4= int(input("Enter num4: "))

if(num1>=num2 and num1>=num3 and num1>=num4):
    print("num1 is the greatest")

elif(num2>=num1 and num2>=num3 and num2>=num4):
    print("num2 is the greatest")

elif(num3>=num1 and num3>=num2 and num3>=num4):
    print("num3 is the greatest")

else:
