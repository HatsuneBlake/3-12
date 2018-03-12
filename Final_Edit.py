class N():
	n = 0
	@classmethod
	def plu(cls):
		cls.n += 1
	@classmethod
	def min(cls):
		cls.n -= 1
	@classmethod
	def pm(cls):
		print 'Numbers of instances created:',cls.n,cls
	def __init__(self):
		self.plu()
	def __del__(self):
		self.min()
		
if __name__ == '__main__':
	a = N()
	b = N()
	print 'I have created 2 instances.\n'
	N.pm()
	del(a)
	print 'Del one of the instance.\n'
	N.pm()