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
		v_sum = 0
		
		v_l_w_zip = zip(lable, self.weight)

		print (list(v_l_w_zip))

		
def f_act(i):
    return 1 if i > 0 else 0


def f_get_tr_add_basedate():
    lables = [[0, 0], [0, 1], [1, 1], [1, 0]]
    vacs = [0, 0, 1, 0]

    return lables, vacs

def train_preceptorn():

	lables, vacs = f_get_tr_add_basedate()

	p = Preceptron(f_act,2)

	p.train(lables,vacs,1,0.2)

	return p


if __name__ == "__main__":
	
	train_preceptorn()