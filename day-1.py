#  Conditional
# if , else, elif

age = int(input("Enter age: "))
if age>= 18:
    print("eligible for voting")
else:
    print("Not eligible")

print("hello")

num = int(input("Enter number: "))

if num%2==0:
    print("Even number")
else:
    print("odd number")

    marks = int(input("Enter marks: "))

    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 35:
        print("pass")
    else:
        print("fail")