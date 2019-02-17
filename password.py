password = 'a123456'

times_left = 3

while times_left > 0:

	times_left = times_left - 1

	input_password = input('Please enter your password: ')

	if input_password == password:
		print('Sucessfully Login!')
		break
	
	else:
		print('Wrong password.')

		if times_left > 0:
			print(times_left, 'remaining.')
		else:
			print('Your account has been blocked!')
