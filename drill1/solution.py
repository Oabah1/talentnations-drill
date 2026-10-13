def solution(celsius):
    # Convert the input to a number using float()
    celsius_val = float(celsius)
    
    # Calculate Fahrenheit using the provided formula
    fahrenheit = (celsius_val * 9 / 5) + 32
    
    # Return the converted value rounded to 2 decimal places
    return round(fahrenheit, 2)

temperature = solution(37)
print(temperature)


def solution(meters):
    # Convert the input to a number using float()
    meters_val = float(meters)
    
    # Calculate centimeters and millimeters
    centimeters = meters_val * 100
    millimeters = meters_val * 1000
    
    # Create and return the exact multi-line string format
    return f"Centimeters: {centimeters}\nMillimeters: {millimeters}"
meter = solution(3)
print(meter)


def solution(kilograms):
    # Convert the input to a number using float()
    kg_val = float(kilograms)
    
    # Calculate grams and pounds
    grams = kg_val * 1000
    pounds = round(kg_val * 2.20462, 2)
    
    # Return the exact multi-line string format
    return f"Kilograms: {kg_val}\nGrams: {grams}\nPounds: {pounds}"
kilogram = solution(2.0)
print(kilogram)
kilogram = ("5")
print(kilogram)


def solution(value):
    try:
        # Attempt to convert the input to a number using float()
        num_val = float(value)
        # Double the value and round to 2 decimal places
        return round(num_val * 2, 2)
    except ValueError:
        # Return the exact string if conversion fails
        return "Invalid number"
result_1 = solution("5")
print(f'Input: ["5"] -> Received: {result_1}')
result_2 = solution("2.5")
print(f'Input: ["2.5"] -> Received: {result_2}')
result_3 = solution("hello")
print(f'Input: ["hello"] -> Received: {result_3}')