import math

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    """Getter Methods"""
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    

def stdDev(arr):
    age_sum = 0
    sum_deviation = 0
    
    for i in arr:
        age_sum += int(i.get_age())
    sum_mean = age_sum / len(arr)
    
    for j in arr:
        num_in_arr = int(j.get_age())
        temp_num = num_in_arr - sum_mean
        deviations = temp_num ** 2
        sum_deviation += deviations
    
    mean_deviation = sum_deviation / len(arr)
    population_deviation = math.sqrt(mean_deviation)
    
    return population_deviation

person1 = Person("Paul", 28)
person2 = Person("Jon", 30)
person3 = Person("Jane", 44)
person4 = Person("J", 12)
person5 = Person("K", 67)

person_arr = [person1, person2, person3, person4, person5]

print(stdDev(person_arr))