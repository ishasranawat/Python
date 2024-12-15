import random
x=random.randint(0,1)
if x==1:
 print("Heads")
else:
 print("Tails")


# identify spam comment 

a="click here"
b="buy now"
c="subscribe"
d="free followers"

message= input("Enter your phrase: ")

if(a in message or b in message or c in message):
  print("spam")

else:
  print("not a spam")


