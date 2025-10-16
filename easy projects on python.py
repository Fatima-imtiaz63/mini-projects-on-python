def get_number():
    """ Return a simple list of integers"""
    return[3, 4, 7, 8, 10, 11, 12]
nums = get_number()
is_even = lambda x:x % 2 ==0
even = [x for x in nums if is_even(x)]
double = lambda x:x *2
doubled = [double(x) for x in even]
print("original:", nums)
print("Even numbers:", even)
print("double even:", doubled)
def sum_list(list):
    total = 0
    for v in list:
        total += v
        return total
    print("Sums of doubled even:" ,sum_list(doubled))
