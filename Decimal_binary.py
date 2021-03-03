def decimal_to_binary():
	display=[]
	decimal=int(input('enter decimal:')) #prompts user for integer value
	d=decimal
	while decimal<=0: #loop until pos. # entered
		print('Enter a positive integer', '\n')
		decimal=int(input('enter decimal:'))
	if decimal==0: display=['0'] #exception for 0's
	while decimal>0:
		if decimal%2==1:display.append('1')
		else:display.append('0')
		decimal=int(decimal//2) #floor division to calculate different place value
	display.reverse() #function executes on #from left-right; to display properly
	display=int(''.join(display))
	print('\n','Decimal Number:',d,'\n','Binary Number:',display,'\n')
decimal_to_binary()
