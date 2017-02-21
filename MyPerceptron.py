class MyPerceptron(object):
	def __init__(self,_initnum_,activation):
		self.activation = activation
		self._initnum_ = _initnum_
	
	def __str__(self):
		return ("_initnum_ = %s" % (self._initnum_))
	'''	
	def doSomething(self,_input_num_):
		return (self.activation(_input_num_+int(self._initnum_)) == 0 and 'Ace') or 'Bob'
	
	'''
	def doSomething(self,_input_num_, str_0 = 'Ace', str_1 = 'Bob'):
		return str_0 if self.activation(_input_num_+int(self._initnum_)) == 0 else str_1

def f(i):
    return int(i) % 2


def _train_add_():
    p = MyPerceptron(2, f)
    return p

if __name__ == "__main__":
	__perceptron_add__ = _train_add_()
	print(__perceptron_add__)
	print('result = %s' % (__perceptron_add__.doSomething(233)))
	print('result = %s' % (__perceptron_add__.doSomething(233,'HAHA','HEIHEI')))

