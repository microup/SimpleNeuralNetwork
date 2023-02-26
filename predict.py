
def CheckPredict(model, inputData, target):
    threshold = 0.5  # threshold for successful prediction

    y_pred = Predict(model, inputData)
    # count the number of successful predictions
    successful_predictions = sum(
        [1 for i in range(len(target)) if abs(y_pred[i]-target[i]) <= threshold])

    # Calculate the success rate/percentage
    success_percent = 100 * successful_predictions / len(target)

    print(f"Model prediction results: {[f'{pred[0]:.2f}' for pred in y_pred]}")
    print(f"Model success rate/percentage: {success_percent:.2f}%")
    

def Predict(model, inputData):
    y_pred = model.predict(inputData, verbose=0)  # predicted values
    return y_pred

def PredictOneValue(model, X, Y):
    y_pred = model.predict([[X, Y]], verbose=0)  # predicted values
    return y_pred[0][0]
