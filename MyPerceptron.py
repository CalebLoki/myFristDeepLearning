class MyPerceptron(object):
    def __init__(self, _initnum_, activation):
        self.activation = activation
        self._initnum_ = _initnum_

    def __str__(self):
        return "_initnum_ = %s" % (self._initnum_)

    def doSomething(self, _initnum_):
        return self.activation(_initnum_)


def f(i):
    return int(i) % 2


def _train_add_():
    p = MyPerceptron(2, f)
    return p


if __name__ == "__main__":
    _perceptron_add_ = _train_add_()
    print(_perceptron_add_)
    print('result = %s' % (_perceptron_add_.doSomething(233)))
