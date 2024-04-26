prompt = '\nWelcome to the movie theater!'
prompt += '\nHow old are you?'
prompt += "\nEnter 'quit' to exit. "

age = ''

while age != 'quit':
    age = input(prompt)
    
    if age == 'quit':
        break
    elif int(age) < 3:
        # age = input(age)
        print('Your ticket is free!')
    
    elif int(age) < 12:
        # age = input(age)
        print('Your ticket is $10')
    
    elif int(age) > 11:
        # age = input(age)
        print('Your ticket is $15')

