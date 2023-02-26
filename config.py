filename = 'my_model.h5'
epochValue = 30000
percentStopTrain = 95

TrainData = [[1, 2], [3, 4], [5, 6], [0, 0],
           [10, 20], [5.7, 20.5], [1000, 0], [2000, 3000]]  # input data

TrainTarget = [3, 7, 11, 0, 30, 26.2, 1000, 5000]  # target value

# input data for testing
InputData = [[7, 8], [45, 10], [199, 20], [1000, 20], [4000, 3000],
          [1.5, 2.7], [5.7, 20.5]]
# expected values
TargetData = [15, 55, 219, 1020, 7000, 4.2, 26.2]
