#filter
list1 = [1,-2,3,-5,8,-3]
newlist = list(filter(lambda e:e>0,list1))
print(newlist)

#map
list2 = [10,20,30,40,50]
list3 = [100,200,300,400,500]

mapped = list(map(lambda l2,l3:l2+l3,list2,list3))
print(mapped)

