def is_prime(number):
    y =[]
    if number == 1:
        return False
    elif number > 1:
        for x in range(2, number):
            if (number % x) == 0:
                 y.append(x)
            else:
                continue
        if len(y) == 0:
            return True
        else:
            return False
    else:
        return False
