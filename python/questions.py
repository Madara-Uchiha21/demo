#1. Write a program to print the given number is odd or even.
num = int(input("Enter a Number : "))
if num % 2==0:
    print(num,"This number is Even.")
else :
    print(num, "This number is Odd.")
print()

# Odd - Even by using def and return function
def ios(j):
    if j % 2 == 0:
        return "Even"
    else:
        return "Odd"

j = int(input("Enter number: "))
result = ios(j)
print("The number", j, "is", result)
print()

#2. Write a program to find the given number is positive or negative.
Num = int(input("Enter a Number : "))
if Num < 0:
    print(Num,"is a Negetive Number. ")
else:
    print(Num, "is a Positive Number.")
print()

# Or by using def and return function
def io(nu):
    if nu < 0:
        return "negative"
    else :
        return "positive"
nu = int(input("Enter number- "))
recall = io(nu)
print("This number is",recall)
print()

#3. Write a program to find if the given number is prime or not.
num1 = int(input("Enter a number to check,if it is Prime number or not."))
if num1 == 1:
    print(num1,"is not Prime Number.")
else:
    for i in range(2,num1):
        if num1 % i ==0:
            print(num1,"is not a Prime number.")
            break
    else:
        print(num1,"is a Prime number.")
print()

#4. Write a program to check if the given number is palindrome or not.
# (This would only applicable for 3digit number)
# As if we get the input of number from tyhe user.
now = int(input("Enter a Number- "))

# We will Transfer it to another variable temporarily
temp = now 

#suppose user entered a certain number as - 123 so we have to
once = (temp%10)*100
tense = ((temp//10)%10)*10
hun = (temp//100)

# Lets add
palindrome = once + tense + hun

if (palindrome == now):
    print("yes",now ,"and",palindrome,"is a palindrome number.")
else:
    print("No",now,"and",palindrome,"is not a palindrome number.")
print()

# Write a program to check if the given number is palindrome or not.
# THE SIMPLE AND UNIVERSALLY APPLICABLE CODE
numb = input("Enter a number: ")
reverse = numb[::-1]
if numb == reverse:
    print(numb,"is aPalindrome.")
else:
    print(numb,"is not a Palindrome.")
print()

