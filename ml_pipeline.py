from src.extract.telco_data import extract_telco_data
from src.transform.transform_data import preprocessing_data
from src.transform.splitting_data import splitting_process
from src.modeling.decision_tree import modeling

if __name__ == "__main__":
    print("===== Start ML Pipeline =====")

    # 1. extract data
    df_telco = extract_telco_data()

    # 2. preprocessing data
    df_telco = preprocessing_data(data=df_telco)

    # 3. splitting data
    X_train, X_test, y_train, y_test = splitting_process(data=df_telco)

    # 4. modeling data
    modeling(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

    print("===== Finished ML Pipeline =====")
