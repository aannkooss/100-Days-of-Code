# List Comprehension
a better way to manipulate lists

 Traditional way of adding one to every element in a list
`numbers = [1,2,3]  
newList = []  
for number in numbers:  
    addOne = number + 1  
    newList.append(addOne)`

Using List Comprehension
`new_list = [new_item for item in list]`

`newList = [number + 1 for number in numbers]`
In 'english': Create a new list where we add n + 1 in the original list

List Comprehension for STRINGS

name = "Angela"
newNameList = [letter for letter in name] #adds each letter to a new list

Conditional List Comprehension
`newList = [newItem for item in list if test]`

# Dictionary Comprehension
`newDict = {newKey:newValue for item in list}` 

`newDict = {newKey:newValue for (key,value) in dict.items if test}`


