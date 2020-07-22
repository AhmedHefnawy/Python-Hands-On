""""
Mutable May change Value
                   >> list , dictionary
Immutable may not
            >> int , flout , String , tuple
"""

# ============ Immutable
x = 30
print ("x = 30 ID" , id(x))  #  x = 30 ID 140710478858816
x = 50
print("x = 50 ID" , id(x))  # x = 50 ID 140710478859456
x = 30
print ("x = 30 ID" , id(x)) # x = 30 ID 140710478858816

# ============== Mutable
dicT = {'name' : "Ahmed" }
print("ID of DIctionary dicT1 :" , id(dicT))
dicT = {'name' : "Ali"}
print("ID of DIctionary dicT2 :" , id(dicT))
""" 
ID of DIctionary dicT1 : 2327936904384
ID of DIctionary dicT2 : 2327936904448 
"""