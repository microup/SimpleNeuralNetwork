import tensorflow as tf
import os
import time

from config import TrainData, TrainTarget, filename, epochValue
from predict import PredictOneValue
from train import Train

start_time = time.time()

model = tf.keras.models.Sequential([
    # input layer with 2 inputs
    tf.keras.layers.InputLayer(input_shape=(2,)),
    tf.keras.layers.Dense(1)  # layer with one output (sum)
])

if os.path.exists(filename):
    model = tf.keras.models.load_model(filename)
else:
    Train(model, TrainData, TrainTarget, epochValue, filename)

# CheckPredict(model, InputData, TargetData)

print(f"Result: {PredictOneValue(model, 0, 0):.2f}")
print(f"Result: {PredictOneValue(model, 0, 1):.2f}")
print(f"Result: {PredictOneValue(model, 98.1, 2.2):.2f}")
print(f"Result: {PredictOneValue(model, 13242, 245):.2f}")
print(f"Result: {PredictOneValue(model, -1, 5):.2f}")
print(f"Result: {PredictOneValue(model, -1, -5):.2f}")
