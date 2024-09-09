# Write a Python program to count the number of characters (character frequency) in a string
name=input('Enter a string:')
name=name.lower()
ch_count={}
for ch in name:
    if ch in ch_count:
        ch_count[ch]+=1
    else:
        ch_count[ch]=1
print(f"{ch_count}")