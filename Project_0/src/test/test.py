'''
map(lambda x_w: x_w[0] * x_w[1],zip(input_vec, self.weights))

'''


def __pulus_one(n):
    return n + 1


def map_test():
    i_arr =  [0, 1, 2, 3]
    j_arr =  [1, 1, 1, 1]

    i = 1
    j = 2

    n_zip = zip(i_arr, j_arr)

    v_m = map(lambda x_w: x_w[0] + x_w[1], n_zip)
    print(list(v_m))


map_test()
