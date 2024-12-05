
def is_prime(func):
    def wrapper(*v):
        sum=0
        org_f=func(*v)
        if org_f>1:
            for i in range(2,org_f):
                if org_f%i==0:
                    print('Составное')
                    sum+=1
                    break
        if sum==0:
            print('Простое')
        return org_f
    return wrapper

@is_prime
def sum_three(*value):
    sum=0
    for i in value:
        sum+=i
    return sum




result = sum_three(2, 3, 6)
print(result)

