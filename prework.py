# Question 1
# Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.


#     def hello_name(user_name):
#         .....

def hello_name(user_name):
    """Says hello to a given username."""
    print(f"Hello_{user_name}!")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


#     def first_odds():
#         .....

def first_odds():
    """Prints odd numbers from 1-100."""
    num = 1
    while num != 101:
        print(num)
        num += 2
    return


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


#     def max_num_in_list(a_list):


def max_num_in_list(a_list):
    """Returns the max number of a given list of integers."""
    return max(a_list)


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


#     def is_leap_year(a_year):


def is_leap_year(a_year):
    """Returns True or False on whether a given year is a leap year."""
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False
    

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.


#     def is_consecutive(a_list):

def is_consecutive(a_list):
    """Checks to see if all numbers in a list are consecutive numbers or not."""
    return sorted(a_list) == list(range(min(a_list), max(a_list)))
