def fibonacci_sequence(n):
    count = 1
    first = 0
    second = 1
    sum = 0
    y = []
    if n == 0:
        return "[]"
    elif n == 1:
        return "[0]"
    elif count < n:
        for count in range(n):
            y.append(first)
            sum = first + second 
            first = second
            second = sum  
    return y
