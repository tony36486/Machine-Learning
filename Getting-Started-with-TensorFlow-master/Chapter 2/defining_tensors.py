"""
import numpy as np
import tensorflow as tf
#create a 1-D tansor
tensor_1d = np.array([1.3,1,4.0,23.99])

print(tensor_1d)
print(tensor_1d[0])
print(tensor_1d[2])

tf_tensor_conv = tf.convert_to_tensor(tensor_1d, dtype=tf.float64)

with tf.Session() as sess:
    print(sess.run(tf_tensor_conv))
    print(sess.run(tf_tensor_conv[0]))
    print(sess.run(tf_tensor_conv[2]))

tf_tensor_holder = tf.placeholder("float64",tensor_1d.shape,name='tf_tensor_holder')

with tf.Session() as sess:
    print(sess.run(tf_tensor_holder, feed_dict={tf_tensor_holder:tensor_1d}))
    print(sess.run(tf_tensor_holder[0], feed_dict={tf_tensor_holder:tensor_1d}))
    print(sess.run(tf_tensor_holder[2], feed_dict={tf_tensor_holder:tensor_1d}))

tf_tensor_cons = tf.constant(tensor_1d)

with tf.Session() as sess:
    print(sess.run(tf_tensor_cons))
    print(sess.run(tf_tensor_cons[0]))
    print(sess.run(tf_tensor_cons[2]))

"""   
#"""
import numpy as np
import tensorflow as tf
#create a 2-D tansor
tensor_2d=np.array([(1,2,3,4),(4,5,6,7),(8,9,10,11),(12,13,14,15)])

print(tensor_2d)
print(tensor_2d[3][3])
print(tensor_2d[0:2,0:2])

tf_tensor_conv = tf.convert_to_tensor(tensor_2d, dtype=tf.float64)

with tf.Session() as sess:
    print(sess.run(tf_tensor_conv))
    print(sess.run(tf_tensor_conv[3][3]))
    print(sess.run(tf_tensor_conv[0:2,0:2]))

tf_tensor_holder = tf.placeholder("float64",tensor_2d.shape,name='tf_tensor_holder')

with tf.Session() as sess:
    print(sess.run(tf_tensor_holder, feed_dict={tf_tensor_holder:tensor_2d}))
    print(sess.run(tf_tensor_holder[3][3], feed_dict={tf_tensor_holder:tensor_2d}))
    print(sess.run(tf_tensor_holder[0:2,0:2], feed_dict={tf_tensor_holder:tensor_2d}))

tf_tensor_cons = tf.constant(tensor_2d)

with tf.Session() as sess:
    print(sess.run(tf_tensor_cons))
    print(sess.run(tf_tensor_cons[3][3]))
    print(sess.run(tf_tensor_cons[0:2,0:2]))
#"""

