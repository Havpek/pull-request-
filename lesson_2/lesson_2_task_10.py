def bank():
    x = int(input('sum '))
    y = int(input('let '))
    for i in range(y):
        x += int(x * 0.1)
    return x
print(bank())
    
