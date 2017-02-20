
class MyPerceptron(object):

	def __init__(self,_initnum_,activation):
		print(_initnum_)
		self.activation = activation
	
	def __str__(self):
		print("_initnum_ = %f" % (self._initnum_))

def f(i):
	return int(i)%2

def _train_add_():
	p = MyPerceptron(2,f)
	return p

if __name__ == "__main__":
	__perceptron_add__ = _train_add_()
	print('result = %s'%(__perceptron_add__))

