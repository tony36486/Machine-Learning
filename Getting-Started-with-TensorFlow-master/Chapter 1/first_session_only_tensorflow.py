#first_session_only_tensorflow.py

import tensorflow as tf

x = tf.constant(1, name='x')
y = tf.Variable(x+9,name='y')

model = tf.global_variables_initializer()
#tf.initialize_all_variables() is deprecated and will be removed after 2017-03-02
#Use `tf.global_variables_initializer` instead.
with tf.Session() as session:
    session.run(model)
    print(session.run(y))
