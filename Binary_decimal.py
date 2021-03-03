def binary_to_decimal():
	count=0
	sum=0
	a=int(input('enter binary number:'))
	b=a
	while a!=0: #find how many # their are in input
		if a%10==0:
			sum+=(0*(2**count)) #use count for exponent value of 2
			count+=1 #increase count for next place value
			a=a//10 #update binary numbers place position
		elif a%10==1:
			sum+=(1*(2**count))
			count+=1
			a=a//10
	print('\n','Binary Number:',b,'\n','Decimal Number:',sum,'\n')
binary_to_decimal()