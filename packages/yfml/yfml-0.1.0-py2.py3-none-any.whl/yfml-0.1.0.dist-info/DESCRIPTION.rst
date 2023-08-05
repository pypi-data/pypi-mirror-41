some simple functions based on tensorflow

#####################
Simple Example here

#####################
import tensorflow as tf
from yfml.layers import *
from yfml.train import *
from yfml.utils import *
from yfml.quick_build import *
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
train_data, train_label = mnist.train.next_batch(50000)
training_data = Data(train_data, train_label)
x = fl_holder([None, 784])
y = fl_holder([None, 10])
if_training = bool_holder()
x_ = reshape(x, [-1, 28, 28, 1])
final = mix_stack('stack', x_, types=['conv2d', 'maxpool2d', 'conv2d', 'maxpool2d', 'fc', 'fc'],
                  shapes=[16, 2, 32, 2, 256, 10], use_batch_norm=False, if_training=if_training,
                  activation_fn='relu', last_activation_fn='softmax')
loss = loss_fn(final, y)
opt = optimize(loss, 0.001, optimizer='adam', regularizer=['l2', 0.001])
accuracy = compute_accuracy(final, y)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(1000):
    training_data.shuffle()
    iter = 50000//100
    avg_acc = 0.
    for j in range(iter):
        xs, ys = training_data.next_batch(100)
        acc, _ = sess.run([accuracy, opt], {x: xs, y: ys, if_training:True})
        avg_acc += acc/iter
    print('accuracy is : ', avg_acc)


