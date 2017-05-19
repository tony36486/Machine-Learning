#handling tensors


#STEP 1 --- PREPARE THE DATA
import matplotlib.image as mp_image
filename = "mumu1.jpg"
input_image = mp_image.imread(filename)

#dimension : chennal of image
print('input dim = {}'.format(input_image.ndim))
#shape : size of image
print('input shape = {}'.format(input_image.shape))
#type : image type
print(type(input_image[0,0,0]))
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(input_image)
plt.show()

import tensorflow as tf
#STEP 2 --- DEFINE THE OPERATIONS 
#my_image = tf.placeholder("uint8",[960,720,3])
my_image = tf.placeholder("uint8",[None,None,3])
#my_image = tf.constant(input_image)
#my_image = tf.convert_to_tensor(input_image, dtype=tf.uint8)
slice = tf.slice(my_image,[100,100,0],[860,620,-1])

#STEP 3 --- RUN OPERATIONS 
with tf.Session() as session:
    result = session.run(slice,feed_dict={my_image: input_image})
    print(result.shape)
    
plt.figure()
plt.imshow(result)
plt.show()

