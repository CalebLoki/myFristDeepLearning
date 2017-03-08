from functools import reduce


def pe_f_test(vec):
	w = 0.5
	v_sum = 0
	for i in vec:
		v_sum = i * w + v_sum
	return v_sum

def m_f_add(a):
	return a+1

def pe_f_test_1(vec):
	w = 0.5
	v_sum = 0
	print(vec)
	return reduce( lambda a,b : a + b,
					list(map(lambda x_w : x_w[0] * x_w[1] ,zip([2,1,3],[2,0,1]))),0.0)

def get_one_vec(vecs):
	v_sum = 0 
	for i in vecs:
		v_sum = pe_f_test_1(i)

	return v_sum

def pe_f_test_2():
	lables = [[0, 0], [0, 1], [1, 1], [1, 0]]
	vacs = [0, 0, 1, 0]
	l = list(zip(lables,vacs))

	for (vac,lable) in l:
		print ("vac = %s, lable = %s" % (str(vac),str(lable)))
		print (list(zip(vac,lable)))

def zip_test():
	a = [1]
	b = [2]

	v_zip = zip(a,b)

	print (list(v_zip))

def for_loop(n):

	return [0.1 for i in range(n)]

if __name__ == "__main__":
	vecs = [1,0]
	vec = 1
#	print (zip_test())	
	print(for_loop(3))