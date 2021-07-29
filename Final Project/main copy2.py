import numpy as np
import random as rd
import itertools

acc0 = 61.878882
latency0 = 16.30464
acc_array = np.array([0.308031, 0.246401, 0.385460, 0.549228, 0.355705,
                      0.020765, 0.041229, 0.034954, 0.067013, 0.135598,
                      0.066404, -0.012060, 0.054933, 0.009343, 0.014635,
                      0.057120, 0.043826, 0.056370, 0.089531, 0.113646,
                      0.005593, 0.025202, 0.027489, 0.003217, 0.013580,
                      0.088727, 0.116691, 0.120979, 0.203725, 0.153543,
                      -0.020289, -0.026291, -0.027556, -0.040638, -0.031194,
                      -0.014607, 0.006102, -0.006670,  0.004494, 0.002630])
latency_array = np.array([-8.06211, -2.69638, -1.13344, -0.22013, -0.55329,
                          -2.32253, -0.90273, -1.01517, -0.54179, -0.30544,
                          -2.33407, -0.94015, -0.11907, 0.01387, -0.27301,
                          2.85597, 1.29418, 0.65506, 0.68359, 0.62364,
                          1.17867, 0.49333, 0.10513, 0.23057, 0.01159,
                          2.15201, 1.01542, 0.70170, 0.87146, 0.45674,
                          1.91980, 0.70742, 0.16173, 0.21330, 0.17648])


# acc & lantency

def get_acc(d1, d2, d3, d4, d5,
            avg_e1, avg_e2, avg_e3, avg_e4, avg_e5,
            avg_k1, avg_k2, avg_k3, avg_k4, avg_k5,
            e1, e2, e3, e4, e5,
            k1, k2, k3, k4, k5):

    x = np.array([d1, d2, d3, d4, d5,
                  avg_e1, avg_e2, avg_e3, avg_e4, avg_e5,
                  avg_k1, avg_k2, avg_k3, avg_k4, avg_k5,
                  e1, e2, e3, e4, e5,
                  k1, k2, k3, k4, k5,
                  (d1 - 1) * avg_e1,
                  (d2 - 1) * avg_e2,
                  (d3 - 1) * avg_e3,
                  (d4 - 1) * avg_e4,
                  (d5 - 1) * avg_e5,
                  d1 * (d1 - 1) * avg_e1,
                  d2 * (d2 - 1) * avg_e2,
                  d3 * (d3 - 1) * avg_e3,
                  d4 * (d4 - 1) * avg_e4,
                  d5 * (d5 - 1) * avg_e5,
                  d1 * avg_k1,
                  d2 * avg_k2,
                  d3 * avg_k3,
                  d4 * avg_k4,
                  d5 * avg_k5])

    return acc0 + sum(x * acc_array)


def get_latency(d1, d2, d3, d4, d5,
                avg_e1, avg_e2, avg_e3, avg_e4, avg_e5,
                avg_k1, avg_k2, avg_k3, avg_k4, avg_k5,
                e1, e2, e3, e4, e5,
                k1, k2, k3, k4, k5):

    x = np.array([d1, d2, d3, d4, d5,
                  avg_e1, avg_e2, avg_e3, avg_e4, avg_e5,
                  avg_k1, avg_k2, avg_k3, avg_k4, avg_k5,
                  e1, e2, e3, e4, e5,
                  k1, k2, k3, k4, k5,
                  d1 * avg_e1,
                  d2 * avg_e2,
                  d3 * avg_e3,
                  d4 * avg_e4,
                  d5 * avg_e5,
                  d1 * avg_k1,
                  d2 * avg_k2,
                  d3 * avg_k3,
                  d4 * avg_k4,
                  d5 * avg_k5])

    return latency0 + sum(x * latency_array)


def get_my_acc(M):
    return get_acc(M[0], M[1], M[2], M[3], M[4],
                   M[5], M[6], M[7], M[8], M[9],
                   M[10], M[11], M[12], M[13], M[14],
                   M[15], M[16], M[17], M[18], M[19],
                   M[20], M[21], M[22], M[23], M[24])


def get_my_latency(M):
    return get_latency(M[0], M[1], M[2], M[3], M[4],
                       M[5], M[6], M[7], M[8], M[9],
                       M[10], M[11], M[12], M[13], M[14],
                       M[15], M[16], M[17], M[18], M[19],
                       M[20], M[21], M[22], M[23], M[24])


def check_range(array):

    # 1. choose depth from [2, 3, 4]:
    #    d1, d2, d3, d4, d5
    # 2. choose expand ratio from [2, 3, 4, 6]:
    #    avg_e1, avg_e2, avg_e3, avg_e4, avg_e5, e1, e2, e3, e4, e5
    # 3. choose kernel size from [3, 5, 7]:
    #    avg_k1, avg_k2, avg_k3, avg_k4, avg_k5, k1, k2, k3, k4, k5

    error = False

    # 檢查depth、expand ration、kernel size是否合規定
    column_name = np.array(['d1', 'd2', 'd3', 'd4', 'd5',
                            'avg_e1', 'avg_e2', 'avg_e3', 'avg_e4', 'avg_e5',
                            'avg_k1', 'avg_k2', 'avg_k3', 'avg_k4', 'avg_k5',
                            'e1', 'e2', 'e3', 'e4', 'e5',
                            'k1', 'k2', 'k3', 'k4', 'k5'])

    depth_error = np.isin(array[0:5], [2, 3, 4],
                          invert=True).tolist()
    for x in column_name[0:5][depth_error]:
        print(x, 'is not in [2, 3, 4]')
        error = True
    expand_ratio_error = np.isin(array[5:10], [2, 3, 4, 6],
                                 invert=True).tolist()
    for x in column_name[5:10][expand_ratio_error]:
        print(x, 'is not in [2, 3, 4, 6]')
        error = True
    kernel_size_error = np.isin(array[11:15], [3, 5, 7],
                                invert=True).tolist()
    for x in column_name[11:15][kernel_size_error]:
        print(x, 'is not in [3, 5, 7]')
        error = True
    expand_ratio_error = np.isin(array[16:20], [2, 3, 4, 6],
                                 invert=True).tolist()
    for x in column_name[16:20][expand_ratio_error]:
        print(x, 'is not in [2, 3, 4, 6]')
        error = True
    kernel_size_error = np.isin(array[21:25], [3, 5, 7],
                                invert=True).tolist()
    for x in column_name[21:25][kernel_size_error]:
        print(x, 'is not in [3, 5, 7]')
        error = True

    return error


# example of "randomly pick a subnet"
best_acc_array = []

# d1, d2, d3, d4, d5 = [4, 4, 4, 4, 3]
# avg_e1, avg_e2, avg_e3, avg_e4, avg_e5 = [6, 4, 3, 4, 4]
# avg_k1, avg_k2, avg_k3, avg_k4, avg_k5 = [7, 5, 5, 7, 5]
# e1, e2, e3, e4, e5 = [4, 6, 4, 3, 4]
# k1, k2, k3, k4, k5 = [3, 7, 7, 7, 3]

# Simulated Annealing


def SA():
    global best_acc_array
    tmp_bst = best_acc_array
    for run in range(1):  # 10
        T = 1
        L = 70
        # LL = 70
        # t = 0
        # TIME = 1000  # 500
        while T > 0.00001:
            # t += 1
            tmp_neighbor = tmp_bst
            T *= 0.995
            # T = max(T * 0.99, 0.35)
            L = max(L * 0.995, 60)
            # LL = max(LL * 0.97, 55)
            for i in range(5):
                neighbor = tmp_bst
                if i == 0:
                    di = rd.randint(0, 4)
                    neighbor[di] = rd.choice([2, 3, 4])
                elif i == 1:
                    di = rd.randint(5, 9)
                    neighbor[di] = rd.choice([2, 3, 4, 6])
                elif i == 2:
                    di = rd.randint(10, 14)
                    neighbor[di] = rd.choice([3, 5, 7])
                elif i == 3:
                    di = rd.randint(15, 19)
                    neighbor[di] = rd.choice([2, 3, 4, 6])
                else:
                    di = rd.randint(20, 24)
                    neighbor[di] = rd.choice([3, 5, 7])

                if get_my_latency(neighbor) <= L and get_my_acc(neighbor) > get_my_acc(tmp_neighbor):
                    tmp_neighbor = neighbor
                elif T > rd.random():
                    tmp_neighbor = neighbor
                # elif get_my_latency(neighbor) <= L and get_my_latency(tmp_neighbor) > L and T > rd.random():
                #     tmp_neighbor = neighbor
                # elif (get_my_latency(neighbor) - LL) / 100 < rd.random() and get_my_latency(neighbor) > 40:
                #     tmp_neighbor = neighbor
            tmp_bst = tmp_neighbor
            if get_my_acc(best_acc_array) <= get_my_acc(tmp_bst) and get_my_latency(tmp_bst) < 60:
                best_acc_array = tmp_bst
            elif get_my_latency(best_acc_array) > get_my_latency(tmp_bst) and get_my_latency(best_acc_array) >= 74:
                best_acc_array = tmp_bst


for r in range(100000):

    d1, d2, d3, d4, d5 = [rd.choice([2, 3, 4]), rd.choice([2, 3, 4]), rd.choice(
        [2, 3, 4]), rd.choice([2, 3, 4]), rd.choice([2, 3, 4])]
    avg_e1, avg_e2, avg_e3, avg_e4, avg_e5 = [rd.choice([2, 3, 4, 6]), rd.choice(
        [2, 3, 4, 6]), rd.choice([2, 3, 4, 6]), rd.choice([2, 3, 4, 6]), rd.choice([2, 3, 4, 6])]
    avg_k1, avg_k2, avg_k3, avg_k4, avg_k5 = [rd.choice([3, 5, 7]), rd.choice(
        [3, 5, 7]), rd.choice([3, 5, 7]), rd.choice([3, 5, 7]), rd.choice([3, 5, 7])]
    e1, e2, e3, e4, e5 = [rd.choice([2, 3, 4, 6]), rd.choice([2, 3, 4, 6]), rd.choice(
        [2, 3, 4, 6]), rd.choice([2, 3, 4, 6]), rd.choice([2, 3, 4, 6])]
    k1, k2, k3, k4, k5 = [rd.choice([3, 5, 7]), rd.choice([3, 5, 7]), rd.choice(
        [3, 5, 7]), rd.choice([3, 5, 7]), rd.choice([3, 5, 7])]

    # d1, d2, d3, d4, d5, avg_e1, avg_e2, avg_e3, avg_e4, avg_e5, avg_k1, avg_k2, avg_k3, avg_k4, avg_k5, e1, e2, e3, e4, e5, k1, k2, k3, k4, k5 = [
    #     4, 2, 4, 4, 3, 2, 2, 2, 2, 6, 3, 3, 5, 7, 7, 2, 4, 4, 4, 3, 3, 5, 7, 5, 3]

    best_acc_array = np.array([d1, d2, d3, d4, d5,
                               avg_e1, avg_e2, avg_e3, avg_e4, avg_e5,
                               avg_k1, avg_k2, avg_k3, avg_k4, avg_k5,
                               e1, e2, e3, e4, e5,
                               k1, k2, k3, k4, k5])

    SA()

    predicted_acc = get_my_acc(best_acc_array)
    predicted_latency = get_my_latency(best_acc_array)

    # check if the architecture is legal
    error = check_range(best_acc_array)

    if not error:
        # if predicted_latency > 60 or predicted_acc < 72.6:
        #     continue
        if predicted_latency > 60 or predicted_acc < 73.5:
            continue
        print(str(r) + ": ")
        print('predicted acc:', predicted_acc, '%')  # 73.904113
        print('predicted latency:', predicted_latency, 'ms')  # 130.53857

        # save subnet architecture
        np.save(str(r) + '_0710006.npy', best_acc_array)
        print(best_acc_array.tolist(), sep=',')
    else:
        print('\nPlease modify the architecture and try again!')
