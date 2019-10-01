acc_details = {'nikita':[203, 123456, 5000],
               'adarsh': [103, 789456, 10000],
               'mandar': [109, 987878, 1000],
               'durvesh': [101, 784512, 25000]}
               #'Morty': [1598, 895623, 15000]}
print('\t\t\t\t\t\t-----WELCOME TO ATM-----\n')
while True:
	s = int(input('Enter the corresponding number: 1. Check balance 2. Deposit money 3. Withdraw money 4. Exit\n'))
	if s==1:
		name,pin = map(str, input('Enter your name and PIN space separated: ').split())
		for k,v in acc_details.items():
			if k == name:
				if v[0] == int(pin):
					print(f'Account number: {v[1]}')
					print(f'Balance: {v[2]}')
				else:
					print('Invalid PIN')
	if s==2:
		name, pin = map(str, input('Enter your name and PIN space separated: ').split())
		for k, v in acc_details.items():
			if k == name:
				if v[0] == int(pin):
					print(f'Account number: {v[1]}')
					money = int(input('Enter amount to be deposited: '))
					v[2]+=money
					print(f'Balance: {v[2]}')
				else:
					print('Invalid PIN')
	if s==3:
		name, pin = map(str, input('Enter your name and PIN space separated: ').split())
		for k, v in acc_details.items():
			if k == name:
				if v[0] == int(pin):
					print(f'Account number: {v[1]}')
					while True:
						money = int(input('Enter amount to be withdrawn: '))
						if v[2]<money:
							print('Insufficient Balance, try again!')
						else:
							v[2]-=money
							print(f'Balance: {v[2]}')
							break
				else:
					print('Invalid PIN')
	if s==4:
		print('Goodbye!')
		break
	print()
