def palindrome(t) :
    if t == text[::-1]:
        print(f"The Input {t} is  Palindrome.")
    else :
        print(f"The Input {t} is not a Palindrome.")

text = input("Enter input for Palindrome check: ")
palindrome(text)