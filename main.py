# def checkequal(n , x):
#     if(n ^ x == 0 ):
#         print("numbers are equal")
#     else:
#         print("numbers are not equal")

# checkequal(1,2)



def find_odd_difference(lst):
    result = 0 
    for num in lst:
        result = result ^ num
    return result

print(find_odd_difference([1,1,2,33]))