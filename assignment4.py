# def falling_distance(time):
#     distance = float((1/2) * (9.8 * (time ** 2)))
#     return distance

# print(falling_distance(3.2))

# def small_sort(first, second, third):
#     if first > second:
#         first, second = second, first
#     if first > third:
#         first, third = third, first
#     if second > third:
#         second, third = third, second
#     print(first, second, third)

# small_sort(19, 3, 5)

def hailstone(num):
    if num == 1:
        return 0
    
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
            count += 1
        else:
            num = int((num * 3) + 1)
            count += 1
    print(count)            

hailstone(3)