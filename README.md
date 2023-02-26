# nyroun_sum

This code represents the implementation of a simple neural network with one input layer, one hidden layer, and one output layer that can predict a target value based on input data.

The config.py file defines the data for training and testing the neural network. The training data is represented as a two-dimensional array TrainData, and the corresponding target values are represented as an array TrainTarget. The test data is represented as a two-dimensional array InputData, and the corresponding expected target values are represented as an array TargetData.

The train.py file contains the Train function, which trains the model based on the defined training data using the Adam optimizer and Mean Squared Error (MSE) loss function. The function also includes a CustomCallback custom callback function, which allows outputting information on the training progress and evaluating the model's success after each epoch.

The utils.py file contains the get_success_rate function, which calculates the percentage of successful predictions made by the model based on the test data and its corresponding target values.

The predict.py file contains the CheckPredict and Predict functions, which are used to check and predict target values, respectively.

To use this neural network, you can use the PredictOneValue function, which takes two input parameters X and Y representing input data for the model and returns the predicted value. You can also use the CheckPredict function, which outputs information on the model's predictions and success on the test data.

In this specific example, the model is trained to predict the sum of two numbers, which are the input data. The neural network can be used to solve various tasks that require predicting values based on input data. For example, it can be used to predict real estate prices based on its characteristics or to predict sales based on historical sales data.

For testing purposes, the following set of numbers is available:

``` python
X_test = [[7, 8], [45, 10], [199, 20], [1000, 20], [4000, 3000], [1.5, 2.7]]  
```

The results of the sum of these numbers are as follows:

``` python
Model prediction results: ['15.00', '55.00', '219.00', '1020.01', '7000.01', '4.20']
Model success rate/percentage: 100.00%
```