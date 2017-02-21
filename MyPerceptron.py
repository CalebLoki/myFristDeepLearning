class MyPerceptron(object):
    def __init__(self, _initnum_, activation):
        self.activation = activation
        self._initnum_ = _initnum_

    def __str__(self):
        return "_initnum_ = %s" % self._initnum_

    '''
    def doSomething(self,_input_num_):
        return (self.activation(_input_num_+int(self._initnum_)) == 0 and 'Ace') or 'Bob'

    '''

    def dosomething(self, _input_num_, str_0='Ace', str_1='Bob'):
        return str_0 if self.activation(_input_num_ + int(self._initnum_)) == 0 else str_1


def f(i):
    return int(i) % 2


def _train_add_():
    p = MyPerceptron(2, f)
    return p


def f_for_test():
    v_arr = [[0, 1], [1, 1], [1, 0], [0, 0]]
    v_arr_1 = [0, 1, 0, 0]
    v_zip = zip(v_arr, v_arr_1)

    for (v, v_1) in v_zip:
        print("v = %s, V_1 = %s" % (v, v_1))


if __name__ == "__main__":
    perceptron_add__ = _train_add_()
    print(perceptron_add__)
    print('result = %s' % (perceptron_add__.dosomething(233)))
    print('result = %s' % (perceptron_add__.dosomething(233, 'HAHA', 'HEIHEI')))

    print('---------------')

    f_for_test()
