from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

DATA_PATH = "/opt/airflow/data/accidents_full.csv"
MODEL_PATH = "/opt/airflow/models/model.pkl"

def load_data():
    df = pd.read_csv(DATA_PATH)
    print("Data loaded:", df.shape)
    return "loaded"

def preprocess():
    print("Preprocessing data...")
    return "preprocessed"

def train_model():
    print("Training model...")

    df = pd.read_csv(DATA_PATH)

    # simple example target (adjust if needed)
    X = df.select_dtypes(include=["number"]).fillna(0)
    y = X.iloc[:, 0]  # dummy target for demo

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    os.makedirs("../models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Model saved at", MODEL_PATH)
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