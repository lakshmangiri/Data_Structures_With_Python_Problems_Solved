# Print the numbers from 1 to 100, Then, if the number is multiple of 3 print "Fizz",
# if the number is multiple of 5 print "Buzz".
# Finally if the number is multiple by both 3 and 5 print "FizzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
        print(i)
    elif i % 3 == 0:
        i = "Fizz"
        print(i)
    elif i % 5 == 0:
        i = "Buzz"
        print(i)
    else:
        print(i)