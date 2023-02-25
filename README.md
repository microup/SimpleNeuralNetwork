# nyroun_sum
Neural Network for Addition of Numbers

This script is an example of a simple neural network that adds two different numbers. It utilizes the TensorFlow library for its operation. In this example, there is a pre-configured neural network located in the "my_model.h5" file that can add any two numbers with a 100% success rate.

For testing purposes, the following set of numbers is available:

``` python
X_test = [[7, 8], [45, 10], [199, 20], [1000, 20], [4000, 3000], [1.5, 2.7]]  
```

The results of the sum of these numbers are as follows:

``` python
Model prediction results: ['15.00', '55.00', '219.00', '1020.01', '7000.01', '4.20']
Model success rate/percentage: 100.00%
```