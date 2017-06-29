# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:23:01 2017

@author: tony
"""
import matplotlib.pyplot as plt
import matplotlib.image as mp_image
import numpy as np
import tensorflow as tf
import os
import sys
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
from tensorflow.python.framework import ops

def file_debug_tool(image_name):
    ## check reid output txt exist
    if os.path.isfile(image_name):
        print(image_name+ "\n" +"image exist")
    else:
        print("image not exist")
        ## end the program
        sys.exit()
        
def im_debug_tool(input_image):
    ## dimension : chennel of image
    print('input dim = {}'.format(input_image.ndim))
    ## shape : size of image
    print('input shape ={}'.format(input_image.shape))
    ## show image
    plt.figure()
    plt.imshow(input_image)
    plt.show()  
    
## Reset graph
ops.reset_default_graph()

## Start a graph session
sess = tf.Session()

## Load prid data
## init list
images_list = []
labels_list = []

## image base
"""
## cam i 
## person j ,limit is 749 cus cam_b have 749 person
for i in ['a','b']:
    folder_names = "prid_2011\single_shot\cam_"+str(i)+"\\"
    ## check image floder exist
    if os.path.isdir(folder_names):
        for j in range(750):
            image_names = folder_names+"person_"+str(j+1).zfill(4)+".png"
            ## check image exist
            if os.path.isfile(image_names):
                ## print debug info
                #my_file = open('prid_data_set.txt','a')
                #my_file.write(image_names+" exist"+"\n")
                #my_file.close()
                ## creating list
                input_image = plt.imread(image_names)
                images_list.append(input_image)
                labels_list.append(j)
            else:
                ## print(image_names+"No image exist")
                break            
    else:
        ## print("No floder exist")
        break
"""
## video base
#"""
## cam i
## person j
## frame k
for i in ['a','b']:
    for j in range(10):
        folder_names = "prid_2011\multi_shot\cam_"+str(i)+"\person_"+str(j+1).zfill(4)+"\\"  
         ## check image floder exist
        if os.path.isdir(folder_names):
            for k in range(250):
                image_names = folder_names+str(k+1).zfill(4)+".png"
                ## check image exist
                if os.path.isfile(image_names):
                    ## print debug info
                    #my_file = open('prid_data_set.txt','a')
                    #my_file.write(image_names+" exist"+"\n")
                    #my_file.close()
                    ## creating list
                    input_image = plt.imread(image_names)
                    images_list.append(input_image)
                    labels_list.append(j+1)
                else:
                    ## print(image_names+" No image exist")
                    break                
        else:
            ## print("No floder exist")
            break
            
#"""   
## tran list to np.array
images_arr = np.array(images_list)
images_list = []
labels_arr = np.array(labels_list)
labels_list = []

## check shape 
print(images_arr.shape)
print(labels_arr.shape)

## creat train and test index
# odd as train 
# even as test
train_index = []
test_index = []
for c in range(len(images_arr)):
    if c%2 == 0:
        test_index.append(c)
    else:
        train_index.append(c)
        
train_index_arr = np.array(train_index)
train_index = []
test_index_arr = np.array(test_index)
test_index = []
## memo:
##    train_image = images_arr[train_index_arr[np.random.choice(len(train_index_arr), size=10)]]
##    train_label = labels_arr[train_index_arr[np.random.choice(len(train_index_arr), size=10)]]
##    test_image = images_arr[test_index_arr[np.random.choice(len(test_index_arr), size=10)]]
##    test_label = images_arr[test_index_arr[np.random.choice(len(test_index_arr), size=10)]]

## Set model parameters
batch_size = 25
learning_rate = 0.005
evaluation_size = 25
image_width = images_arr[0].shape[1]
image_height = images_arr[0].shape[0]
target_size = max(labels_arr) + 1
num_channels = images_arr[0].shape[2] # greyscale = 1 channel
generations = 500
eval_every = 5
conv1_features = 25
conv2_features = 50
max_pool_size1 = 2 # NxN window for 1st max pool layer
max_pool_size2 = 2 # NxN window for 2nd max pool layer
fully_connected_size1 = 100

## Declare model placeholders
x_input_shape = (batch_size, image_height, image_width, num_channels)
x_input = tf.placeholder(tf.float32, shape=x_input_shape)
y_target = tf.placeholder(tf.int32, shape=(batch_size))
eval_input_shape = (evaluation_size,  image_height, image_width, num_channels)
eval_input = tf.placeholder(tf.float32, shape=eval_input_shape)
eval_target = tf.placeholder(tf.int32, shape=(evaluation_size))

## Declare model parameters
conv1_weight = tf.Variable(tf.truncated_normal([4, 4, num_channels, conv1_features],
                                               stddev=0.1, dtype=tf.float32))
conv1_bias = tf.Variable(tf.zeros([conv1_features], dtype=tf.float32))

conv2_weight = tf.Variable(tf.truncated_normal([4, 4, conv1_features, conv2_features],
                                               stddev=0.1, dtype=tf.float32))
conv2_bias = tf.Variable(tf.zeros([conv2_features], dtype=tf.float32))

## fully connected variables
resulting_width = image_width // (max_pool_size1 * max_pool_size2)
resulting_height = image_height // (max_pool_size1 * max_pool_size2)
full1_input_size = resulting_width * resulting_height * conv2_features
full1_weight = tf.Variable(tf.truncated_normal([full1_input_size, fully_connected_size1],
                          stddev=0.1, dtype=tf.float32))
full1_bias = tf.Variable(tf.truncated_normal([fully_connected_size1], stddev=0.1, dtype=tf.float32))
full2_weight = tf.Variable(tf.truncated_normal([fully_connected_size1, target_size],
                                               stddev=0.1, dtype=tf.float32))
full2_bias = tf.Variable(tf.truncated_normal([target_size], stddev=0.1, dtype=tf.float32))

## Initialize Model Operations
def my_conv_net(input_data):
    # First Conv-ReLU-MaxPool Layer
    conv1 = tf.nn.conv2d(input_data, conv1_weight, strides=[1, 1, 1, 1], padding='SAME')
    relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_bias))
    max_pool1 = tf.nn.max_pool(relu1, ksize=[1, max_pool_size1, max_pool_size1, 1],
                               strides=[1, max_pool_size1, max_pool_size1, 1], padding='SAME')

    # Second Conv-ReLU-MaxPool Layer
    conv2 = tf.nn.conv2d(max_pool1, conv2_weight, strides=[1, 1, 1, 1], padding='SAME')
    relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_bias))
    max_pool2 = tf.nn.max_pool(relu2, ksize=[1, max_pool_size2, max_pool_size2, 1],
                               strides=[1, max_pool_size2, max_pool_size2, 1], padding='SAME')

    # Transform Output into a 1xN layer for next fully connected layer
    final_conv_shape = max_pool2.get_shape().as_list()
    final_shape = final_conv_shape[1] * final_conv_shape[2] * final_conv_shape[3]
    flat_output = tf.reshape(max_pool2, [final_conv_shape[0], final_shape])

    # First Fully Connected Layer
    fully_connected1 = tf.nn.relu(tf.add(tf.matmul(flat_output, full1_weight), full1_bias))

    # Second Fully Connected Layer
    final_model_output = tf.add(tf.matmul(fully_connected1, full2_weight), full2_bias)
    
    return(final_model_output)

model_output = my_conv_net(x_input)
test_model_output = my_conv_net(eval_input)

## Declare Loss Function (softmax cross entropy)
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=model_output, labels=y_target))

## Create a prediction function
prediction = tf.nn.softmax(model_output)
test_prediction = tf.nn.softmax(test_model_output)

## Create accuracy function
def get_accuracy(logits, targets):
    batch_predictions = np.argmax(logits, axis=1)
    num_correct = np.sum(np.equal(batch_predictions, targets))
    return(100. * num_correct/batch_predictions.shape[0])

## Create an optimizer
my_optimizer = tf.train.MomentumOptimizer(learning_rate, 0.9)
train_step = my_optimizer.minimize(loss)

## Initialize Variables
init = tf.global_variables_initializer()
sess.run(init)

## Start training loop
train_loss = []
train_acc = []
test_acc = []
for i in range(generations):
    rand_index = np.random.choice(len(train_index_arr), size=batch_size)
    rand_x = images_arr[train_index_arr[rand_index]]
    #rand_x = np.expand_dims(rand_x, 3)
    rand_y = labels_arr[train_index_arr[rand_index]]
    train_dict = {x_input: rand_x, y_target: rand_y}
    
    sess.run(train_step, feed_dict=train_dict)
    temp_train_loss, temp_train_preds = sess.run([loss, prediction], feed_dict=train_dict)
    temp_train_acc = get_accuracy(temp_train_preds, rand_y)
    
    if (i+1) % eval_every == 0:
        eval_index = np.random.choice(len(test_index_arr), size=evaluation_size)
        eval_x = images_arr[test_index_arr[rand_index]]
        #eval_x = np.expand_dims(eval_x, 3)
        eval_y = labels_arr[test_index_arr[rand_index]]
        test_dict = {eval_input: eval_x, eval_target: eval_y}
        test_preds = sess.run(test_prediction, feed_dict=test_dict)
        temp_test_acc = get_accuracy(test_preds, eval_y)
        
        # Record and print results
        train_loss.append(temp_train_loss)
        train_acc.append(temp_train_acc)
        test_acc.append(temp_test_acc)
        acc_and_loss = [(i+1), temp_train_loss, temp_train_acc, temp_test_acc]
        acc_and_loss = [np.round(x,2) for x in acc_and_loss]
        print('Generation # {}. Train Loss: {:.2f}. Train Acc (Test Acc): {:.2f} ({:.2f})'.format(*acc_and_loss))
        
# Matlotlib code to plot the loss and accuracies
eval_indices = range(0, generations, eval_every)
# Plot loss over time
plt.figure()
plt.plot(eval_indices, train_loss, 'k-')
plt.title('Softmax Loss per Generation')
plt.xlabel('Generation')
plt.ylabel('Softmax Loss')
plt.show()

# Plot train and test accuracy
plt.figure()
plt.plot(eval_indices, train_acc, 'k-', label='Train Set Accuracy')
plt.plot(eval_indices, test_acc, 'r--', label='Test Set Accuracy')
plt.title('Train and Test Accuracy')
plt.xlabel('Generation')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

# Plot some samples
plt.figure()
actuals = rand_y[0:6]
predictions = np.argmax(temp_train_preds,axis=1)[0:6]
images = np.squeeze(rand_x[0:6])

Nrows = 2
Ncols = 3
for i in range(6):
    plt.subplot(Nrows, Ncols, i+1)
    plt.imshow(np.reshape(images[i], [128,64,3]), cmap='Greys_r')
    plt.title('Actual: ' + str(actuals[i]) + ' Pred: ' + str(predictions[i]),
                               fontsize=10)
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)