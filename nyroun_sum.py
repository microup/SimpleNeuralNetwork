import tensorflow as tf
import os

model = tf.keras.models.Sequential([
    # input layer with 2 inputs
    tf.keras.layers.InputLayer(input_shape=(2,)),
    tf.keras.layers.Dense(1)  # layer with one output (sum)
])

filename = 'my_model.h5'

if os.path.exists(filename):
    model = tf.keras.models.load_model(filename)
else:    
    model.compile(optimizer='adam', loss='mse')

    X_train = [[1, 2], [3, 4], [5, 6], [0, 0], [10, 20]]  # input data
    y_train = [3, 7, 11, 0, 30] # target value

    model.fit(X_train, y_train, epochs=10000, verbose=0)

    model.save(filename)

# input data for testing
X_test = [[7, 8], [45, 10], [199, 20], [1000, 20], [4000, 3000],
          [1.5, 2.7]]  
# expected values
y_test = [15, 55, 219, 1020, 7000, 4.2]  

y_pred = model.predict(X_test)  # predicted values
threshold = 0.5  # threshold for successful prediction

# count the number of successful predictions
successful_predictions = sum(
    [1 for i in range(len(y_test)) if abs(y_pred[i]-y_test[i]) <= threshold])

# Calculate the success rate/percentage
success_percent = 100 * successful_predictions / len(y_test)

print(f"Model prediction results: {[f'{pred[0]:.2f}' for pred in y_pred]}")
print(f"Model success rate/percentage: {success_percent:.2f}%")
