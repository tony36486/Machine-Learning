#programmimg_model.py

import tensorflow as tf

a = tf.placeholder("int32")
b = tf.placeholder("int32")

y = tf.multiply(a,b)

"""
#tf 0.71 mul() = tf 1.0 multiply()  
sess = tf.Session()

print(sess.run(y, feed_dict={a:2,b:5})) 
#python2.7 print = python3.6 print()
"""
model = tf.global_variables_initializer()
with tf.Session() as session:
    merged = tf.summary.merge_all()
    #tf.merge_all_summaries() is deprecated and will be removed after 2016-11-30.
    #Please switch to tf.summary.merge_all.
    writer = tf.summary.FileWriter("H:\\my_TFpath\\tensorflowlogs",session.graph)
    print("H:\\my_TFpath\\tensorflowlogs") #H:\my_TFpath\tensorflowlogs
    #tf.train.SummaryWriter is deprecated, instead use tf.summary.FileWriter
    session.run(model)
    print(session.run(y, feed_dict={a:2,b:5}))

