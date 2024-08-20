from typing import Tuple
from sklearn.model_selection import train_test_split
import pandas as pd


def splitting_process(
    data: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Function that will split the train and test into 80:20 proportion

    Parameters
    ----------
    data (pd.DataFrame): data telco that split into training and testing

    Returns
    -------
    X_train (pd.DataFrame): features data for training data
    X_test (pd.DataFrame): features data for test data
    y_train (pd.Series): target for training data
    y_test (pd.Series): target for test data
    """
    # determine the features and the target
    X = data.drop(["churn"], axis=1)
    y = data["churn"]

    print("===== Start Splitting Data =====")

    # before split the data, we check the data shape for features and target
    print(f"Features Shape: {X.shape}")
    print(f"Target Shape: {y.shape}")

    # define the test size and random seed number
    TEST_SIZE = 0.2
    SEED = 42

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=SEED
    )

    # validate the shape for train and test data

    print(f"Train Features Shape: {X_train.shape}")
    print(f"Test Features Shape: {X_test.shape}")
    print(f"Train Target Shape: {y_train.shape}")
    print(f"Test Target Shape: {y_test.shape}")

    print("===== Finished splitting data =====")

    return X_train, X_test, y_train, y_test
