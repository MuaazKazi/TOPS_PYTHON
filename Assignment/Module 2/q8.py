# Write a Python program to test whether a passed letter is a vowel or not
# inp=input("Enter words:")
# vowel={'a','e','i','o','u'}
# if inp.islower() in vowel:
#     print("vowel")
# else:
#     print("input has not vowel")


inp=input("Enter words:")
vowel={'a','e','i','o','u'}
inp=inp.lower()
for ch in inp:
    if ch in vowel:
        print(f"{ch} is Vowel")
    else:
        print(f"{ch} is not vowel")

