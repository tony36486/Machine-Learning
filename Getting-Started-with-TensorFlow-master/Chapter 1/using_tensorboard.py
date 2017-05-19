#using_tensorboard.py

import tensorflow as tf

a = tf.constant(10,name="a")
b = tf.constant(90,name="b")
y = tf.Variable(a+b*2,name='y')
model = tf.global_variables_initializer()

with tf.Session() as session:
    merged = tf.summary.merge_all()
    #tf.merge_all_summaries() is deprecated and will be removed after 2016-11-30.
    #Please switch to tf.summary.merge_all.
    writer = tf.summary.FileWriter("H:\\my_TFpath\\tensorflowlogs",session.graph)
    print("H:\\my_TFpath\\tensorflowlogs") #H:\my_TFpath\tensorflowlogs
    #tf.train.SummaryWriter is deprecated, instead use tf.summary.FileWriter
    session.run(model)
    print(session.run(y))



