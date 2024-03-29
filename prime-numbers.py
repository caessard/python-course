

def run():
    number = int(input('Digite un número: '))
    result = is_prime(number)

    if result is True:
        print('El número digitado es primo')
    else:
        print('El número digitado NO es primo')

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
            
    return True

if __name__ == '__main__':
    run()