from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

#DATA_PATH = "/opt/airflow/data/accidents_full.csv"
DATA_PATH = "/opt/airflow/data/preprocessed"
MODEL_PATH = "/opt/airflow/models/model.pkl"
 
    
def load_data():
    df = pd.read_csv("/opt/airflow/data/preprocessed/X_train.csv")
    #df = pd.read_csv(DATA_PATH)
    print("Train data loaded:", df.shape)
    return "loaded"
    #print("Data loaded:", df.shape)
    #return "loaded"


def preprocess():
    print("Preprocessing data...")
    return "preprocessed"


def train_model():
    print("Training model...")

    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    import joblib
    import os

    # Load already prepared datasets
    X_train = pd.read_csv("/opt/airflow/data/preprocessed/X_train.csv")
    y_train = pd.read_csv("/opt/airflow/data/preprocessed/y_train.csv")

    # FIX: remove train_test_split (NOT needed)

    model = RandomForestClassifier(n_estimators=50)
    model.fit(X_train, y_train.values.ravel())

    os.makedirs("/opt/airflow/models", exist_ok=True)

    joblib.dump(model, "/opt/airflow/models/model.pkl")

    print("Model saved at /opt/airflow/models/model.pkl")

    return "trained"


with DAG(
    dag_id="accident_pipeline_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    t2 = PythonOperator(
        task_id="preprocess",
        python_callable=preprocess
    )

    t3 = PythonOperator(
        task_id="train_model",
        python_callable=train_model
    )

    t1 >> t2 >> t3