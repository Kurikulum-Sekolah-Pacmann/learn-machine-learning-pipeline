from src.utils.helper import init_engine
import pandas as pd


def extract_telco_data() -> pd.DataFrame:
    """
    Function for read data from Telco Data Warehouse

    Returns
    -------
    df_telco (pd.DataFrame): data telco
    """
    try:
        # create engine
        wh_conn = init_engine()

        # read data
        query = "select * from telco_churn"

        df_telco = pd.read_sql(sql=query, con=wh_conn)

        return df_telco

    except Exception as e:
        raise Exception(e)

    finally:
        wh_conn.dispose()
