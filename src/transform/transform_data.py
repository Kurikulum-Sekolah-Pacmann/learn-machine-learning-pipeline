import pandas as pd


def preprocessing_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function for preprocessing process based on the requirements

    Parameters
    ----------
    data (pd.DataFrame): dataframe that will be preprocess

    Returns
    -------
    data (pd.DataFrame): dataframe that already been preprocess
    """
    data = data.drop(["customerID"], axis=1)

    RENAME_COLS = {
        "SeniorCitizen": "senior_citizen",
        "Partner": "partner",
        "Dependents": "dependents",
        "Tenure": "tenure",
        "PhoneService": "phone_service",
        "MultipleLines": "multiple_lines",
        "InternetService": "internet_service",
        "OnlineSecurity": "online_security",
        "OnlineBackup": "online_backup",
        "DeviceProtection": "device_protection",
        "TechSupport": "tech_support",
        "StreamingTV": "streaming_tv",
        "StreamingMovies": "streaming_movies",
        "Contract": "contract",
        "PaperlessBilling": "paperless_billing",
        "PaymentMethod": "payment_method",
        "MonthlyCharges": "monthly_charges",
        "TotalCharges": "total_charges",
        "Churn": "churn",
    }

    data = data.rename(columns=RENAME_COLS)

    # Mapping "Yes" to 1 and "No" to 0 in specific columns
    COLS_TO_MAP = [
        "partner",
        "dependents",
        "phone_service",
        "paperless_billing",
        "churn",
    ]

    VALUES_TO_MAP = {"Yes": 1, "No": 0}

    print("===== Start Mapping Values =====")

    for col in COLS_TO_MAP:
        data[col] = data[col].map(VALUES_TO_MAP)

    print("===== Finish Mapping Values =====")

    data["total_charges"] = data["total_charges"].replace({" ": 0})

    # create dictionary to mapping a data type

    CAST_COLUMNS = {
        "tenure": "int",
        "monthly_charges": "float",
        "total_charges": "float",
    }

    data = data.astype(CAST_COLUMNS)

    CHECK_COLS = [
        "gender",
        "multiple_lines",
        "internet_service",
        "contract",
        "payment_method",
        "online_security",
        "online_backup",
        "device_protection",
        "tech_support",
        "streaming_tv",
        "streaming_movies",
    ]

    data = pd.get_dummies(data, columns=CHECK_COLS)

    return data
