class Preceptron(object):
    def __init__(self, activation, _iniunm_):
        self.activation = activation

        # 初始化权重和偏置值;
        self.weight = [0.0 for itme in range(_iniunm_)]
        self.bias = 0.0

    def __str__(self):
        return "[weight = %s, bias = %s] " % (self.weight, self.bias)


def f_act(i):
    return 1 if i > 0 else 0


def f_get_tr_add_basedate():
    lables = [[0, 0], [0, 1], [1, 1], [1, 0]]
    vacs = [0, 0, 1, 0]

    return lables, vacs
