celsius = input('Input degrees (ONLY INTEGERS!) in Celsius: ')
try: 
    celsius = float(celsius)
    
    fahrenheit = celsius * 1.8 + 32
    print(f"The temperature in fahrenheit is {fahrenheit}")
except:
    print('Please, input valid number')