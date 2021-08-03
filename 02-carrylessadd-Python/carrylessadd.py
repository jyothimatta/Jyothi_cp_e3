# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	return Add(x, y, 0)
def Add(x,y,digit):
    if x == 0 and y == 0:
        return 0
    add = (x %10 + y%10)%10
    return add * 10**digit + Add(x//10, y//10, digit+1)

