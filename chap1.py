"""Exercise 1.1.
Whenever you are experimenting with a new feature, you should try to make mistakes. For example,
in the “Hello, world!” program, what happens if you leave out one of the quotation marks? What if
you leave out both? What if you spell print wrong?
This kind of experiment helps you remember what you read; it also helps when you are programming,
because you get to know what the error messages mean. It is better to make mistakes now and on
purpose than later and accidentally.
1. In a print statement, what happens if you leave out one of the parentheses, or both?
2. If you are trying to print a string, what happens if you leave out one of the quotation marks,
or both?
3. You can use a minus sign to make a negative number like -2. What happens if you put a plus
sign before a number? What about 2++2?
4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python?
What about 011?
5. What happens if you have two values with no operator between them?
"""
print("Hello, world") 
print(2++2) ## +2 số dương, kq = 4
'''
print(09) ## SyntaxError
print(011) ## SyntaxError
print(2 3) ## SyntaxError
'''

"""
Exercise 1.2. Start the Python interpreter and use it as a calculator.
1. How many seconds are there in 42 minutes 42 seconds?
2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
mile in minutes and seconds)? What is your average speed in miles per hour?
"""
m = s = 42
total = (m * 60 ) + s
print(total) ## 2562

k = 10
miles = k/ 1.61
print(miles) ## 6.211180124223602

average_pace = ( 42 + ( 42 / 60 )) / 6.21
print(average_pace) ## 6.876006441223833

average_speed = 6.21 / (( 42 + ( 42 / 60 )) / 60 )
print(average_speed) ## 8.725995316159251
