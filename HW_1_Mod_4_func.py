# ex #4 from auto
# <--------------------------------->

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price * (1 - discount)
#
#     apply_discount()
#     return price
#
# print (discount_price(100, 0.44))


# ex #5 from auto
# <--------------------------------->

# def get_fullname (first_name, last_name, middle_name=''):
#   if middle_name != '':
#     fullname = first_name + ' ' + middle_name + ' ' +  last_name
#   else:
#     fullname = first_name + ' ' +  last_name
#   return fullname


# ex #6 from auto
# <--------------------------------->

# def format_string(string, length):
#   if len(string) >= length:
#     return string
#   else:
#     new_string = ' ' * ((length - len(string)) // 2) + string
#     return new_string


# ex #11 from auto
# <--------------------------------->

# def fibonacci(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print (fibonacci(8))
