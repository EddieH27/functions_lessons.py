def tea_order(customer_name, tea_type, **kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for key, value in kwargs.items():
        print(" - Add", key, ":", value)
#tea_order("Alice", "chamomile")
#tea_order("bob", "black", milk="oat")
tea_order("Tony", "black", milk="oat", sweetener="honey")
# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
def sum_squares(*args):
    sum = 0
    for num in args:
        sum += num **2
    return sum
print(sum_squares(2, 4, 6, 8, 10, 12))

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of argum0ents, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    sum = 0
    for num in args:
        sum += abs(num)
    return sum
print(absolute_sum(-10, 5, -3, 7, -2))
list_of_numbers = [-1, -2, -3, 4, 5]
print(absolute_sum(*list_of_numbers))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.
def personal_numbers(name, *args):
    sum_numbers = 0
    for num in args:
        sum_numbers += num
    return f"{name}, the sum of your numbers is {sum_numbers}"
print(personal_numbers("John", 1, 2, 3, 4, 5))
# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"