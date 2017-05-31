import random as rd
import pickle

INPUTS = []
OUTPUTS = []


def equation(w, x, y, z):
    first = x * y
    second = w + first + z
    return second / 2

    #
    # for i in 100000:
    #
    #     4 random numbers

def create_data(num: int):
    global INPUTS
    global OUTPUTS


    for i in range(num):
        w = rd.randint(1, 1000)
        x = rd.randint(1, 5000)
        y = rd.randint(1, 25000)
        z = rd.randint(1, 100000)
        INPUTS.append([w,x,y,z])

        answer = equation(w, x, y, z)

        OUTPUTS.append([answer])

create_data(100000)

train_x = INPUTS[:60000]
train_y = OUTPUTS[:60000]

test_x = INPUTS[60000:]
test_y = OUTPUTS[60000:]

with open('data_set.pickle', 'wb') as f:
    pickle.dump([train_x , train_y, test_x, test_y], f)



# def main():
