# def get_average():
#     num1 = float(input("Please enter the first of 5 numbers: "))
#     num2 = float(input("Next: "))
#     num3 = float(input("Next: "))
#     num4 = float(input("Next: "))
#     num5 = float(input("Next: "))
    
#     average = float((num1 + num2 + num3 + num4 + num5) / 5)
    
#     print(average)

# get_average()


# def temp_converter(cel):
#     far = (((9/5) * cel) + 32)
#     print(far)

# temp_converter(-10.5)

# def change_converter(cents):
#     change_dict = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}
#     while cents > 0:
#         if cents >= 25:
#             cents -= 25
#             change_dict["quarters"] = change_dict.get("quarters", 0) + 1
#         elif cents >= 10:
#             cents -= 10
#             change_dict["dimes"] = change_dict.get("dimes", 0) + 1
#         elif cents >= 5:
#             cent -= 5
#             change_dict["nickels"] = change_dict.get("nickels", 0 ) + 1
#         elif cents >= 1:
#             cents -= 1
#             change_dict["pennies"] = change_dict.get("pennies", 0 ) + 1
#     return change_dict

# print(change_converter(87))

def change_converter(cents):
    quarters = int(cents / 25)
    cents = cents % 25
    
    dimes = int(cents / 10)
    cents = cents % 10
    
    nickels = int(cents / 5)
    cents = cents % 5
    
    pennies = int(cents / 1)
    cents = cents % 1
    
    print(f"Q: {quarters}, D: {dimes}, N: {nickels}, P: {pennies}")

change_converter(87)