def get_success_rate(model, X_test, y_test, threshold=0.5):
    y_pred = model.predict(X_test, verbose=0)  # predicted values
    successful_predictions = sum(
        [1 for i in range(len(y_test)) if abs(y_pred[i]-y_test[i]) <= threshold])
    success_percent = 100 * successful_predictions / len(y_test)
    return success_percent
