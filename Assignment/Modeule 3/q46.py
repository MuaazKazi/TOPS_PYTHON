# Write a Python program to combine values in python list of dictionaries.
data=[{'item': 'item1', 'amount': 400},
{'item': 'item2', 'amount':300}, 
{'item': 'item1', 'amount': 750}]
result={}
for r in data:
    item=r['item']
    amount=r['amount']
    if item in result:
        result[item]+=amount
    else:
        result[item]=amount
print("Result:",result)