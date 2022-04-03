txt = input()
storeVar = ""
#your code goes here
result = txt.split(' ')
for list_item in result:
    if len(storeVar) <= len(list_item):
        storeVar = list_item

print(storeVar)
