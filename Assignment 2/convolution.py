from __future__ import absolute_import

import os
import tensorflow as tf
import numpy as np
import random
import math

def conv2d(inputs, filters, strides, padding):
	"""
	Performs 2D convolution given 4D inputs and filter Tensors.
	:param inputs: tensor with shape [num_examples, in_height, in_width, in_channels]
	:param filters: tensor with shape [filter_height, filter_width, in_channels, out_channels]
	:param strides: MUST BE [1, 1, 1, 1] - list of strides, with each stride corresponding to each dimension in input
	:param padding: either "SAME" or "VALID", capitalization matters
	:return: outputs, NumPy array or Tensor with shape [num_examples, output_height, output_width, output_channels]
	"""
	if hasattr(inputs, "numpy"):
		inputs = inputs.numpy()
	if hasattr(filters, "numpy"):
		filters = filters.numpy()
	inputs = np.array(inputs)
	filters = np.array(filters)

	num_examples, in_height, in_width, input_in_channels = inputs.shape
	filter_height, filter_width, filter_in_channels, filter_out_channels = filters.shape
	assert input_in_channels == filter_in_channels, ("input in_channels ({}) must equal filter in_channels ({})".format(input_in_channels, filter_in_channels))

	num_examples_stride, strideY, strideX, channels_stride = strides

	# Cleaning padding input
	if padding == "SAME":
		padY = (filter_height - 1) // 2
		padX = (filter_width - 1) // 2
	elif padding == "VALID":
		padY = 0
		padX = 0
	else:
		raise ValueError("padding must be 'SAME' or 'VALID'")

	padded_inputs = np.pad(inputs, ((0, 0), (padY, padY), (padX, padX), (0, 0)))

	# Calculate output dimensions

	pass


