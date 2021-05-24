from superuser import admin

adm=admin()
print ('***WELCOME TO THE QUIZ***')


while True:
	print('1.enter as admin\n2.enter as candidate\n3.exit')
	choice=int(input())
	password=0000
	if choice==1:
		p=int(input('enter the password: '))
		if p==password:
			adm.set_qs()
			adm.set_ans()
		else:
			print('incorrect password')

	elif choice==2:
		adm.start_quiz()

	elif choice==3:
		print('Hope to see you soon')
		break

	else:
		print('enter a valid input')
