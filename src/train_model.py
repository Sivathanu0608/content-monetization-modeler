from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np
import joblib

from src.database import get_data
from src.preprocessing import preprocess_data


def train_models():
    print("Loading data...")
    df = get_data()

    print("Preprocessing data...")
    df, _ = preprocess_data(df)

    # ---------- FEATURES & TARGET ----------
    X = df.drop(columns=['ad_revenue_usd', 'video_id', 'date'])
    y = df['ad_revenue_usd']

    # ---------- TRAIN TEST SPLIT ----------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---------- MODELS ----------
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "SVR": SVR(),
        "KNN": KNeighborsRegressor()
    }

    results = {}

    print("\nTraining models...\n")

    for name, model in models.items():
        print(f"Training {name}...")

        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        r2 = r2_score(y_test, predictions)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        mae = mean_absolute_error(y_test, predictions)

        results[name] = {
            "model": model,
            "r2": r2,
            "rmse": rmse,
            "mae": mae
        }

        print(f"{name} -> R2: {r2:.4f}, RMSE: {rmse:.2f}, MAE: {mae:.2f}\n")

    # ---------- SELECT BEST MODEL ----------
    best_model_name = max(results, key=lambda x: results[x]["r2"])
    best_model = results[best_model_name]["model"]

    print(f"Best Model: {best_model_name}")

    # ---------- SAVE MODEL ----------
    joblib.dump(best_model, "models/model.pkl")
    print("Model saved as models/model.pkl")

    return results