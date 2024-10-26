#print("Hello world")

#calculator App

print("Basic calculator")
print("""
      1.Addition
      2.Subtraction
      3.Multiplication
      4.Division""")
choice=int(input("Enter your choice:"))
num_1=int(input("Enter number 1:"))
num_2=int(input("Enter number 2:"))
if(choice==1):
    print(num_1+num_2)
elif(choice==2):
    print(num_1-num_2)
elif(choice==3):
    print(num_1*num_2)
else:
    print(num_1/num_2)

