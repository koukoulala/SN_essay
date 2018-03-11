import tensorflow as tf
import numpy as np

reader = tf.train.NewCheckpointReader('model/data-00000-of-00001')
all_variables = reader.get_variable_to_shape_map()
w1 = reader.get_tensor("conv1/weights")
print(type(w1))
print(w1.shape)
print(w1[0])