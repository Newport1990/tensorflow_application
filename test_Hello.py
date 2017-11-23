#/#!/usr/bin/env

#/*
# *@author: CH
# *@date: 2017.11.21
# *@description: Just a Demo of Tensorflow
# */
# 

import tensorflow as tf
hello = tf.constant('Hello World!')
sess = tf.Session()
print(sess.run(hello))