file=open("sample.txt","r")
first_n_lines=file.readlines()
print(first_n_lines[:3])
file.close()