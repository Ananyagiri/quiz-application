class admin:

	def __init__(self):
		self.lv=None
		self.l1=[]
		self.l2=[]
		self.l3=[]
		self.a1=[]
		self.a2=[]
		self.a3=[]
		self.dict_easy={}
		self.dict_intermidiate={}
		self.dict_difficult={}
		self.l=None
		self.a=None
		self.score=0


	def set_qs(self):
		print('Please choose the difficulty level\n1.easy\n2.intermidiate\n3.difficult\n4.exit')
		self.lv=int(input())
		if self.lv==1:
			self.l=self.l1
		elif self.lv==2:
			self.l=self.l2
		elif self.lv==3:
			self.l=self.l3
		elif self.lv==4:
			return None
		else:
			print('choose a valid option')
			return admin.set_qs(self)


		if self.l!=[]:
			print('you cannot add into this quiz, it is already added')
			return admin.set_qs(self)
		else:
			pass


		while True:
			n=int(input('enter the total number of question:  '))
			for i in range(n):
				print('print the qstn with 4 options marked by a/b/c/d and separated by comma(,) i.e:\nwhich direction does the sun rise,a.east,b.west,c.north,d.south')
				i=input().split(',')
				for j in i:
					print(j)
				self.l.append(tuple(i))
			break

	def set_ans(self):
		if self.lv==1:
			self.a=self.a1
			
		elif self.lv==2:
			self.a=self.a2
			
		elif self.lv==3:
			self.a=self.a3

		elif self.lv==4:
			return None

			

		while True:
			print('now set the answers for every question')
			for x in self.l:
				print(x)
				ans=input('a/b/c/d')
				self.a.append(ans)
				print()
			if self.lv==1:
				self.dict_easy=dict(zip(self.l,self.a))
			elif self.lv==2:
				self.dict_intermidiate=dict(zip(self.l,self.a))
			elif self.lv==3:
				self.dict_difficult=dict(zip(self.l,self.a))

			break
		


	def start_quiz(self):
		print('Please choose the difficulty level\n1.easy\n2.intermidiate\n3.difficult\n4.exit')
		t=int(input())
		if t==1:
			d=self.dict_easy
		elif t==2:
			d=self.dict_intermidiate
		elif t==3:
			d=self.dict_difficult
		elif t==4:
			return None
		else:
			print('choose a valid option')
			return admin.start_quiz(self)

#		while True:
		if d=={}:
			print('the quiz is not added yet')
			return admin.start_quiz(self)
		else:
			pass
			
		while True:
			for i in d:
				print(i)
				answ=input('enter the answer (a/b/c/d)')
				if answ==d[i]:
					self.score+=1
					print('correct answer, your score is',self.score)
					print('your final score is', self.score)
				else:
					print('wrong answer, your score is',self.score)
					print('your final score is', self.score)
			break
				



