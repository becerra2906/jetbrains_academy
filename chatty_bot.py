### basic chat bot project done for jetbrains academy python learning route

name = "Aid"
created_at = "2020"
greeting_1 = "Hello! My name is {}".format(name)
greeting_2 = "I was created in {}".format(created_at)

print(greeting_1)
print(greeting_2)
print('Please, remind me your name.')

name = input()

name_message = 'What a great name you have {}!'.format(name)

print(name_message)
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

message = "Your age is {}; that's a good time to start programming!".format(age)

print(message)
