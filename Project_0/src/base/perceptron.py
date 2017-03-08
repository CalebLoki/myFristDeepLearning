from functools import reduce

class Preceptron(object):
	def __init__(self, activation, _iniunm_):
		self.activation = activation

		# 初始化权重和偏置值;
		self.weight = [0.0 for itme in range(_iniunm_)]
		self.bias = 0.0

	def __str__(self):
		return ("[weight = %s, bias = %s] " % (self.weight, self.bias))

	def train(self,lables,vacs,iterator,rate):
		for i in range(iterator):
			self.single_opreater(lables,vacs,rate)

	def single_opreater(self,lables,vacs,rate):

		v_lables_vacs_zip = zip(lables,vacs)

		for (lable,vac) in v_lables_vacs_zip:
			self.forcast(lable)

	def forcast(self, lable):
		v_l_w_zip = zip(lable, self.weight)

		v_sum = list(map(lambda x_y: x_y[0] * x_y[1] , zip(lable, self.weight)))

		print (v_sum)

		
def f_act(i):
    return 1 if i > 0 else 0


def f_get_tr_add_basedate():
    lables = [[0, 0], [0, 1], [1, 1], [1, 0]]
    vacs = [0, 0, 1, 0]

    return lables, vacs

def train_preceptorn():

	p = Preceptron(f_act,2)
	
	lables, vacs = f_get_tr_add_basedate()

	p.train(lables,vacs,1,0.2)

	return p


if __name__ == "__main__":
	
	and_perception = train_preceptorn()

	print(and_perception)

	# 测试
	'''
	print('1 and 1 = %s' % (and_perception.forcast([1, 1])))
	print('0 and 0 = %d' % (and_perception.forcast([0, 0])))
	print('1 and 0 = %d' % (and_perception.forcast([1, 0])))
	print('0 and 1 = %d' % (and_perception.forcast([0, 1])))
	'''