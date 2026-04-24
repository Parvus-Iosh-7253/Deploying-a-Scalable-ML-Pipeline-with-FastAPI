import pytest
from train_model import data, X_train, X_test, model, p, r, fb

def test_model_metrics_values():
    """
    Test to ensure all metrics are correctly calculated.
    Expected:
    - all score values should be between 0 and 1 inclusive
    """

    assert 0.0 <= p <= 1.0
    assert 0.0 <= r <= 1.0
    assert 0.0 <= fb <= 1.0


def test_training_testing_size():
    """
    Test to ensure training and testing data are of correct dimensions.
    Expected:
    - Both are 108 columns wide after being encoded (done at creation in the process_data function)
    - X_train should have a number of rows = 80% of the raw data
    - X_test should have a number of rows = 20% of the raw data
    """

    assert X_train.shape[1] == 108
    assert X_test.shape[1] == 108

    assert round(X_train.shape[0] / data.shape[0], 1) == 0.8
    assert round(X_test.shape[0] / data.shape[0], 1) == 0.2


def test_model_type():
    """
    Test to ensure ML model is of the expected build.
    Expected:
    - model type is RandomForestClassifier
    """
    
    assert model.__class__.__name__ == "RandomForestClassifier"
