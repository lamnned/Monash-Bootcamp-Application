IntList = [8,5,3,1]

def ListToInt(IntList: list) -> int: 
    result = 0 
    for num in IntList:
        if type(num) is int:
            result = result * 10 + num
        else: 
            raise TypeError
    return result 

print(ListToInt(IntList))

# TEST CASES FOR DIGIT NO. #
assert(ListToInt([1]) == 1) # 1 digit number
assert(ListToInt([1,2]) == 12) # 2 digit number
assert(ListToInt([1,2,3]) == 123) # 3 digit number
assert(ListToInt([1,2,3,4]) == 1234) # 4 digit number

# HALTS AT PROBLEM INSTANCES #
try:
    ListToInt([1,"2",3,4])  # strings
except TypeError:
    pass 

try:
    ListToInt([1,2.0,3,4])  # floats
except TypeError:
    pass 
try:
    ListToInt([1,(2,3),3,4])  # tuples
except TypeError:
    pass 