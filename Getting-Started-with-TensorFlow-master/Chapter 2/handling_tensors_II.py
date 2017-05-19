#handling tensors second example


#STEP 1 --- PREPARE THE DATA
import matplotlib.image as mp_image
filename = "mumu1.jpg"
input_image = mp_image.imread(filename)

#dimension : chennal of image
print('input dim = {}'.format(input_image.ndim))
#shape : size of image
print('input shape = {}'.format(input_image.shape))

height,width,depth= input_image.shape

import matplotlib.pyplot as plt
plt.figure()
plt.imshow(input_image)
plt.show()
#STEP 2 --- DEFINE THE OPERATIONS 
import tensorflow as tf

# 4 method: transform image to tansors 。 select one
x = tf.Variable(input_image)
#x = tf.constant(input_image)
#x = tf.convert_to_tensor(input_image, dtype=tf.uint8)
#x = tf.placeholder("uint8",[None,None,3])

"""
model = tf.initialize_all_variables()
initialize_all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed after 2017-03-02.
Use `tf.global_variables_initializer` instead.
"""
#if you use Variable open ,if you don't close
model = tf.global_variables_initializer()

#STEP 3 --- RUN OPERATIONS 
with tf.Session() as session:
    #if you use placeholder open ,if you don't close
    #x=session.run(x,feed_dict={x: input_image})
    
    x = tf.transpose(x, perm=[1,0,2])
    
    #if you use Variable open ,if you don't close
    session.run(model)
    
    result=session.run(x)
    
plt.figure()
plt.imshow(result)
plt.show()


