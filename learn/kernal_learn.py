import tensorflow as tf

input = tf.Variable([
    [1.0, 2.0, 3.0, 4.0],
    [5.0, 6.0, 7.0, 8.0],
    [8.0, 7.0, 6.0, 5.0],
    [4.0, 3.0, 2.0, 1.0]])
input=tf.reshape(input,[1,4,4,1])
filter = tf.Variable(tf.random_normal([2,2,1,1]))

op = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='VALID')
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(input))
    print(sess.run(op))

sess.close()