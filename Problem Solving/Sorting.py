""""
Sorting algorithm in python
ordering data collection
list is apply to sort
tuple is not ; tuple is an immutable object Can't change >> Sorting Changning things Not create a new one  * IN PLACE *.... you can by Using Sorted ()

"""

list_data = ["asfas" , "effr" , "iytughjy" , "nhjup" , "zwertr" , "qweasd" , "tcdfd" , "vcgrfdfv"]
# order data alphabitically order
list_data.sort()
print("Ordered List :" , list_data)

# Order data in revers order
list_data.sort(reverse = True)
print("Reversed Order :" , list_data)

print(help(list.sort))
""""
sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.
 
 key = < Sorting function >   
reverse = False >> sort in ascending order
reverse = True  >> sort in descending order

"""

# ==================== Complex Examble ===============

# list
Plants = [
    ("Zerf" , 225 , 6866.48 , 48.14) ,
    ("Wgrg" , 95.3 , 987.3 ,4.8885 ),
    ("Gefe" , -63.41448 , 35.56 , 74.8496),
    ("Agrev" , 25.15848 , 872.36 , 478.6959),
    ("Tfeb" , 12.00548 , 124 , 6546)
]
# let's to order Plant on second value
size = lambda Plants : Plants[1] # it's meaning we detect the second value in list
Plants.sort(key=size , reverse= False)
print("The new plants is :" , Plants)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""""
List.sort() Change the list
Q : Can you create a sorted copy ?
q : Can you sort a tuple ?
>>>>>>> Ans > Use Sorted( iterable  , / , *  , Key = Non , Revers = False)
"""

# let's Sorte a list in new copy list
old_list = ["Q" , "I" , "X" , "A" , "F" , "Z" , "B"]
copy_sorted_list = sorted(old_list)
print("the mean list :" , old_list)
print("the copy list :" , copy_sorted_list)

# let's sort a tuple
data_tuple = (7,5,6,8,2,1,4,36,3,82,58,2,95,52,9,194,9,94,4,9,4,954,9,964,9,6,555)
print("The old tuple is:" , data_tuple)
print("Sorted tuple is :" , sorted(data_tuple)) #the sorted tuple is list #######



""""
YOU CAN SORT A STRING THAT WILL RETURN A LIST CONTAIN ALPHABITICAL ORDER ELEMENTS
"""
print("ZYXSDFHRKYUTYJT" , "///" , "Sorted alpha :" , sorted("ZYXSDFHRKYUTYJT" , reverse=True))


















