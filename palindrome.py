n=input("Enter the string : ").strip()
n=n.casefold()
if n==n[::-1]:
    print(n,end=" is a palindrome")
else:
    print(n,end=" is not a palindrome")