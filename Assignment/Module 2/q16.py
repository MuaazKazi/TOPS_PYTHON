# Write a Python program to count the occurrences of each word in a given sentence
name=input('Enter a string:')
name=name.lower()
name=name.split()
ch_count={}

for ch in name:
    if ch in ch_count:
        ch_count[ch]+=1
    else:
        ch_count[ch]=1
print(f"{ch_count}")