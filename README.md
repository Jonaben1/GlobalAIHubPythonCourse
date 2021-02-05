# GlobalAIHubPythonCourse
#To write a list of prime numbers from 0-100 using functions



def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
        return True
    
    
    
def get_primes(start, stop):
    my_list=[]
    for i in range (start, stop):
        if is_prime(i) == True:
            my_list.append(i)
    return my_list

get_primes(0, 100)
