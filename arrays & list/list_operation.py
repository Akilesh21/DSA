li = [] # ----empty list
li  = [1,2,3]
print(type(li))
li = [1,2,"Akilesh"] #----multitype of list 
print(li)


#ACCESS AND CHANGE ELEMENTS IN LIST
print(li[1]) #----accesing specific list elements through index
li[2] = "Umesh" #---change elements of list through index
print(li)
#we can change the elements which are in the list through index
 
#slicing
print(li[0:2]) #--- we can give specific range to print the data in list
print(li[1:])
print(li[1:10])

#insert and append elements in list

li.append("Ankush") # it will add the element in the last
print(li)
li.insert(1,7)
print(li)
#it will insert 7 in the 1 index
#extend 
li.append([9,10,11]) # append won't take multiple elements if you want to add multiple elements in list thrpugh append it will take  a list we use extend for that purpose
print(li)
li.extend([9,10,11])
print(li)

#remove elements from list
li.remove(7)
print(li) # it will remove that element which are present in list and it will remove first present element in the list if multiple same elements are there

li.pop()
print(li)  #we can delete  the element from list it will bydefault remove last elements if index is not given
li.pop(1)
print(li) 

print(li[1])