# def even_number_of_evens(numbers):
#     return False

# assert even_number_of_evens([]) == False, "No numbers"
# assert even_number_of_evens([2]) == False, "One even number"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multible numbers, three even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multible numbers, four even"
# assert even_number_of_evens([1,3,9]) == False, "No even numbers"

# def is_even(number):
#     return number % 2 == 0
    
# def even_number_of_evens(numbers):
    
#     evens = sum([1 for n in numbers if is_even(n)])
#     return False if evens == 0 else is_even(evens)
    
# assert even_number_of_evens([]) == False, "No numbers"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2]) == False, "One even number"
# assert even_number_of_evens([1,3,9]) == False, "Three odd numbers"    
    

# assert even_number_of_evens([]) == False, "No numbers"
# assert even_number_of_evens([2]) == False, "One even number"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
# assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"


# def even_number_of_evens(numbers):
#     if numbers == []:
#       return False
#     else:
#         evens = 0
    
#     for the_amount_of_numbers in numbers:
#         if the_amount_of_numbers % 2 == 0:
#             evens += 1
#     if evens == 0:
#         return False
#     else:    
#         return evens %2 == 0        




def is_even(number):
    return number % 2 == 0
        
def even_number_of_evens(numbers):
    
    evens = 0
    for each_number in numbers:
        if is_even(each_number):
            evens += 1
    if evens == 0:
        return False
    else:    
        return is_even(evens)        
        
#  THIS CODE IS PYTHONIC OR IDIOMATIQUE PYTHON----IF UR COMFORTABLE WITH LIST COMPREHENSIONS---
#  IT REDUCES ALL OF THE CODE ABOVE INTO 2 LINES
#     evens = sum([1 for n in numbers if is_even(n)])
#     return False if evens == 0 else is_even(evens)                
    
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([1, 3, 9]) == False, "Three odd numbers"
print("All tests passed!")
