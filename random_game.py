import random

guessesTaken = 0
print('Првет, игрок! Как тебя зовут?')
Name = input()

number = random.randint(1, 10)
print("Ну что, " + Name +  "! Я загадываю число от 1 до 10")

for guessesTaken in range(6):
    try:  
        print('Попробуй угадать _')
        guess = int(input())
    except ValueError:
        print('Введите число цифрами, а то АТАТА будет!')
        guess = int(input())
    
    
    if guess < number:
        print('Нюююю, твоё число слишком маленькое..)')
        
    if guess == number:
        break
    
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Вау, молодец ' + Name + '! Ты справился за ' + guessesTaken + ' попытки!')
    
if guess != number:
    number = str(number)
    print('Увы. Я загадал число ' + number + '.')
    
