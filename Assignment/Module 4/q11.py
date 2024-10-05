# Write a Python program to write a list to a file
list=['nine','ten','eleven','twelve']
file=open('sample.txt','a')
result='\n'.join(list)
file.write(f"\n{result}\n")