def fizz_buzz(number):
    # checks if the number is divisible by both 3 and 5 and returns FizzBuzz
    if number%15 == 0:
        return "FizzBuzz"
    # checks if the number is divisible by 3
    elif number%3 == 0:
        return "Fizz"
    # checks if the number is divisible by 5
    elif number%5 == 0:
        return "Buzz"
    else:
        return number
        # print statement for all the condition
print fizz_buzz(30)
print fizz_buzz(9)
print fizz_buzz(5)
print fizz_buzz(4)
