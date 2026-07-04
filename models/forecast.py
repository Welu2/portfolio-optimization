import numpy as np
import pandas as pd


def forecast_lstm(model, last_sequence, scaler, steps=180):
    """
    Iteratively forecast future values using a trained LSTM model.
    """
    predictions = []

    current_sequence = last_sequence.copy()

    for _ in range(steps):
        pred = model.predict(
            current_sequence.reshape(1, current_sequence.shape[0], 1),
            verbose=0,
        )

        predictions.append(pred[0, 0])

        current_sequence = np.append(current_sequence[1:], pred)

    predictions = np.array(predictions).reshape(-1, 1)
    predictions = scaler.inverse_transform(predictions)

    return predictions.flatten()


def confidence_interval(predictions, residual_std):
    lower = predictions - 1.96 * residual_std
    upper = predictions + 1.96 * residual_std
    return lower, upper