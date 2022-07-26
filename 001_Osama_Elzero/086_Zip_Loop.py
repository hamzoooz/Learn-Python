list1 = [1, 2, 3, 4 ]
list2 = ["A", "B", "C" ]
tuple1 = ("hamza", "Banga", "Ahmed")
dict1 = {"name":"hamzoooz", "Age": 23, "cuntry":"sudan"}

# ulutimateList = zip(list1, list2)
# for item1  in ulutimateList:
    # print(item1)

for item1, item2, item3,item4 in zip(list1, list2, tuple1, dict1 ):
    print(item1)
    print(item2)
    print(item3)
    print( item4, "=>" , dict1[item4])
