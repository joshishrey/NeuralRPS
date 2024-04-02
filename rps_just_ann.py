#data import 
history=[]
with open('history.txt', "r") as f:
  for line in f:
    history.append(line.strip())
se=[[] for i in range(len(history)-4)]
out=[]

# take last 3 games as input 
for co in range(3, len(history)-1):
    tem=[]
    tem.append((int(history[co-3][1])))
    tem.append((int(history[co-3][4])))
    tem.append((int(history[co-2][1])))
    tem.append((int(history[co-2][4])))
    tem.append((int(history[co-1][1])))
    tem.append((int(history[co-1][4])))
    se[co-3]+=tem
    #take the current index user input as output 
    out.append(int(history[co][1]))
siz=len(history)-4
import tensorflow as tf

#input placeholders
x_ = tf.placeholder(tf.float32, shape=[siz,6], name="x-input")
y_ = tf.placeholder(tf.float32, shape=[siz], name="y-input")

#ann stuff (theta are weights )
#pretty generic stuff no big fuss 
Theta1 = tf.Variable(tf.random_uniform([6,6], -1, 1), name="Theta1")
Theta3 = tf.Variable(tf.random_uniform([6,6], -1, 1), name="Theta3")
Theta2 = tf.Variable(tf.random_uniform([6,1], -1, 1), name="Theta2")

Bias1 = tf.Variable(tf.zeros([6]), name="Bias1")
Bias3 = tf.Variable(tf.zeros([6]), name="Bias3")
Bias2 = tf.Variable(tf.zeros([1]), name="Bias2")

A2 = tf.nn.relu(tf.matmul(x_, Theta1) + Bias1)
A3 = tf.matmul(A2, Theta3) + Bias3

#this is the output of the ann
Hypothesis = tf.matmul(A3, Theta2) + Bias2


#this is the main part The cost and the training steps 
cost = tf.reduce_mean(tf.square(y_ -Hypothesis))
#current aim to minimize cost 
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cost)


#then again generic stuff

X = se
Y = out

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(100000):
        sess.run(train_step, feed_dict={x_: X, y_: Y})
        if i % 1000 == 0:
            print('Epoch ', i)
            print('Hypothesis ', sess.run(Hypothesis, feed_dict={x_: XOR_X, y_: XOR_Y}))
           # print('Theta1 ', sess.run(Theta1))
          #  print('Bias1 ', sess.run(Bias1))
          #  print('Theta2 ', sess.run(Theta2))
          #  print('Bias2 ', sess.run(Bias2))
            print('cost ', sess.run(cost, feed_dict={x_: XOR_X, y_: XOR_Y}))

