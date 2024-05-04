current_users = ['slavetomints', '248011', 'daisy', 'admin', 'alistair']

new_users = ['John', 'alistair', 'Jim','James', 'Daisy']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry, that username is taken. Please select a new one.')
    else:
        print(f'Welcome {new_user}')