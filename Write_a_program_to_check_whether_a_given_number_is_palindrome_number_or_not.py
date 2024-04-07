#Write a program to check whether a given number is palindrome number or not

number=int(input("Enter the number:"))
num=number
rev_num=0
while num>0:
    rev_num=(rev_num*10)+(num%10)
    num=num//10
    if number==rev_num:
        print("number {} is a palindrome ".format(number))
    else:
        print("number {} is not a palindrome ".format(number))

