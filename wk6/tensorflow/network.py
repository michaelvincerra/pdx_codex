import pickle
import tflearn
import tflearn.datasets.mnist as mnist



def equation(w, x, y, z):
    first = x * y
    second = w + first + z
    return second / 2


train_x, train_y, test_x, test_y = mnist.load_data(one_hot=True)

# pickle.load(open('data_set.pickle','rb'))

# print(len(train_x))
# print(len(train_y))
# print(len(test_x))
# print(len(test_y))
#

number_nodes = 500


network= tflearn.input_data(shape=[None, 784])# first one is always None;
network = tflearn.fully_connected(network, number_nodes)
network = tflearn.fully_connected(network, number_nodes)
network = tflearn.fully_connected(network, 10, activation='softmax')   # '1' defines the output layer
network = tflearn.regression(network, )

model = tflearn.DNN(network, tensorboard_verbose=0)
model.load('./best_model')

model.fit(train_x, train_y, n_epoch=4, batch_size=1000, show_metric=True, validation_set=(test_x, test_y))

model.save('best_model')

# model.save('best_model')

def format_pred(prediction):
    pred = prediction[0]
    index= 0
    max =pred[0]
    for i in range(len(pred)):
        if pred[i] > max:
            index = i

    return index

print(test_y[0])
print(format_pred(model.predict([test_x[0]])))
