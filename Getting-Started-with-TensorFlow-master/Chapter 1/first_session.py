#first_session.py

#a simple Python code
x = 1
y = x + 9
print(y)

#....and the tensorflow translation of the previous code
import tensorflow as tf
#set a constant x = 1
x = tf.constant(1, name='x')
#set a variable y = x + 1
y = tf.Variable(x+9,name='y')
print(y)

