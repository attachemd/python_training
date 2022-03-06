from re import L


L1 = ['ADMIN', 'SUPER_ADMIN', 'MANAGER']
L2 = ['ADMIN','MANAGER']
L22 = [{'name':'ADMIN'}, {'name':'MANAGER'}]
L3 = [1,2]
# print( not not[i for i in L1 if i in L22])
print( [i for i in L1 for j in L22 if i == j["name"]])
print( not not[i for i in L1 for j in L22 if i == j["name"]])
# for i in L1:
#     for j in L22:
#         if(i == j["name"]):
#             print(i)

# # Python3 code to iterate over a list
# list = [1, 3, 5, 7, 9]
  
# # Using for loop
# for i in list:
#     print(i)