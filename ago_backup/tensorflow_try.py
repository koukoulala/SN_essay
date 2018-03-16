# 引入必要的module
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib

import numpy as np
import tensorflow as tf

# Data sets
TRAINING = "tmp/bcspwr/train3.csv"

TEST = "tmp/bcspwr/test3.csv"

def main():
  #https://cloud.tencent.com/developer/article/1005381   csv文件首行前两列分别表示数据组的个数和每个数据组的特征数
  # Load datasets.
  training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=TRAINING,
      target_dtype=np.int,
      features_dtype=np.float32)
  test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=TEST,
      target_dtype=np.int,
      features_dtype=np.float32)

  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=8)]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,hidden_units=[10, 20, 10],n_classes=8,model_dir="/tmp/t3")

  # Define the training inputs
  def get_train_inputs():
    x = tf.constant(training_set.data)
    y = tf.constant(training_set.target)
    return x, y

    # Define the test inputs
  def get_test_inputs():
    x = tf.constant(test_set.data)
    y = tf.constant(test_set.target)
    return x, y

  for i in range(20):
    # Fit model.
    classifier.fit(input_fn=get_train_inputs, steps=200)

      # 输出训练集准确度，看看是否有过拟合现象
    accuracy_score = classifier.evaluate(input_fn=get_train_inputs, steps=1)["accuracy"]
    print("第",i,"次的Train Accuracy: {0:f}\n".format(accuracy_score))

    # Evaluate accuracy.
    accuracy_score = classifier.evaluate(input_fn=get_test_inputs, steps=1)["accuracy"]
    print("第",i,"次的Test Accuracy: {0:f}\n".format(accuracy_score))


if __name__ == "__main__":
    main()