def fizz_buzz(number):
    if number%15 == 0:
        return "FizzBuzz"
    elif number%3 == 0:
        return "Fizz"
    elif number%5 == 0:
        return "Buzz"
    else:
        return number
print fizz_buzz(30)
print fizz_buzz(9)
print fizz_buzz(5)
print fizz_buzz(4)
