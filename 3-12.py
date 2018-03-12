class N():
	n = 0
	def count(cls):
		cls.n += 1
	count = classmethod(count)
	def pm(cls):
		print 'n of instances:',cls.n,cls
	pm = classmethod(pm)
	def __init__(self):
		self.count()

class S(N):
	n = 0
	def __init__(self):
		N.__init__(self)

class SS(N):
	n = 0
	def __init__(self):
		N.__init__(self)
	
if __name__ == '__main__':
	a,b,c,d,e = N(),S(),SS(),SS(),N()
	for i in (N,S,SS):
		i.pm()