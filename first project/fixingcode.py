# Step 1: Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import logging
import shap
import mlflow
import optuna
from optuna import create_study
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# Step 2: Set Up Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 3: Load the Dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    logging.info("Dataset loaded successfully.")
    return data

data = load_data('path/to/your/dataset.csv')

# Step 4: Preprocess the Data
def preprocess_data(data):
    X = data.drop('target_column', axis=1)
    y = data['target_column']
    
    categorical_features = X.select_dtypes(include=['object']).columns.tolist()
    numerical_features = X.select_dtypes(include=[np.number]).columns.tolist()

    # Handle missing values
    X[numerical_features] = X[numerical_features].fillna(X[numerical_features].mean())
    X[categorical_features] = X[categorical_features].fillna('Unknown')

    # Create a preprocessing pipeline
    numerical_transformer = Pipeline(steps=[('scaler', StandardScaler())])
    categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )
    
    return X, y, preprocessor

X, y, preprocessor = preprocess_data(data)

# Step 5: Define a Deep Learning Model
def create_model(input_shape):
    model = keras.Sequential([
        layers.Input(shape=input_shape),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Change activation based on your task
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Step 6: Hyperparameter Optimization with Optuna
def objective(trial):
    model = create_model(input_shape=X.shape[1])
    n_epochs = trial.suggest_int('n_epochs', 10, 100)
    batch_size = trial.suggest_categorical('batch_size', [16, 32, 64])

    history = model.fit(X, y, epochs=n_epochs, batch_size=batch_size, validation_split=0.2, verbose=0)
    accuracy = model.evaluate(X, y, verbose=0)[1]
    return accuracy

study = create_study(direction='maximize')
study.optimize(objective, n_trials=10)
logging.info(f'Best hyperparameters: {study.best_params}')

# Step 7: Evaluate the Best Model
best_model = create_model(input_shape=X.shape[1])
best_model.fit(X, y, epochs=study.best_params['n_epochs'], batch_size=study.best_params['batch_size'])
y_pred = (best_model.predict(X) > 0.5).astype("int32")

# Step 8: Evaluation Metrics
print(classification_report(y, y_pred))
sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# Step 9: Explainability with SHAP
explainer = shap.KernelExplainer(best_model.predict, X)
shap_values = explainer.shap_values(X)
shap.summary_plot(shap_values, X)

# Step 10: Save the Best Model with Timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_filename = f'best_model_{timestamp}.h5'
best_model.save(model_filename)
logging.info(f"Best model saved as {model_filename}.")

# Step 11: Log the Experiment with MLflow
mlflow.start_run()
mlflow.log_param("model", "Deep Learning")
mlflow.log_param("best_params", study.best_params)
mlflow.log_metric("accuracy", accuracy)
mlflow.log_artifact(model_filename)
mlflow.end_run()
