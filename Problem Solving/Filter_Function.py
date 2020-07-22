import statistics
""""
data (d) : list or tuple or any data collection 
function(Filter key) : mean or median or any filter key
-------------- you want to filter all data collection in filter key 
filter (function , data ) 
"""

# examble one is fiter data in mean average

# data .......
data = [1.3 , 2.5 , 2.8 , 6 , -1.0 , -0.1]
#filter key
avg = statistics.mean(data)
print("The mean of the Data listed is =" , avg)

#the function that detect the using of the filter key into filter function
print(list(filter(lambda x : x > avg , data))) # X >> refers to the element from data list
print(list(filter(lambda x : x < avg , data))) # X >> refers to the element from data list

# <<<<<<<<<<<<<<<<<<<< Remove missing data >>>>>>>>>>>>>>>>>>>>>>>
# data list ...
countries = ["" , "Egypt" , "" , "" , "America" , "Colombia" , "Chile" , "" , "Franch" , "" , "" ]
print("Filterimg the missing data from data list >> ",list(filter(None , countries)))

""""
the mising data is the false values and ^^
False Value
"" , 0 , 0.0 , [] , () , {} , False , None 

"""



