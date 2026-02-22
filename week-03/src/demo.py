from utils import capitalize, truncate, clamp, is_prime, average, factorial
from validators import is_email, is_phone_number, is_valid_age, is_valid_date


print('Utils demonstrācija')
# capitalize
print(f'capitalize("python") -> {capitalize("python")}')
# truncate
print(f'truncate("Programmēšana", 6) -> {truncate("Programmēšana", 6)}')
# clamp
print(f'clamp(3, 5, 20) -> {clamp(3, 5, 20)}')
# is_prime
print(f'is_prime(29) -> {is_prime(29)}')
# average
print(f'average([5, 15, 25, 35]) -> {average([5, 15, 25, 35])}')
# factorial (derīgs)
print(f'factorial(5) -> {factorial(5)}')
# factorial ar kļūdu (nederīgs)
try:
    print(f'factorial(-5) -> {factorial(-5)}')
except Exception as e:
    print(f'factorial(-5) -> {type(e).__name__}: {e}')


print('\nValidators demonstrācija')
# is_email
print(f'is_email("skola@edu.lv") -> {is_email("skola@edu.lv")}')
# is_phone_number
print(f'is_phone_number("+371 29123456") -> {is_phone_number("+371 29123456")}')
# is_valid_age
print(f'is_valid_age(12) -> {is_valid_age(12)}')
# is_valid_date (derīgs datums – garais gads)
print(f'is_valid_date("2024-02-29") -> {is_valid_date("2024-02-29")}')
# is_valid_date (nederīgs datums)
print(f'is_valid_date("2023-02-29") -> {is_valid_date("2023-02-29")}')